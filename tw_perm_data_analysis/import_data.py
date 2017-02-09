# __author__ = 'ktc312'
#  -*- coding: utf-8 -*-
# coding: utf-8
import pandas as pd
import os
import datetime
import data_cleaning
import download_data

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tw_perm_data_analysis/')


def read_csv_to_list(file_name):
    with open(data_path+'data/'+file_name) as f:
        the_list = [line.rstrip('\n') for line in f]
    list_of_lists = []
    for i in the_list:
        the_list = i.split(',')
        list_of_lists.append(the_list)
    final_list = []
    for i in list_of_lists:
        list_sliced = [i[0][2:-1], i[1][2:-2]]
        final_list.append(list_sliced)
    return final_list


def list_to_csv(the_list, file_name):
    f = open(data_path + 'data/' + file_name, "w")
    f.write("\n".join(map(lambda x: str(x), the_list)))
    f.close()


def logging_updates(rows_before, found_rows, new_rows):
    update_log = read_csv_to_list('update_log.csv')
    update_log[0][1] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    update_log[1][1] = str(rows_before)
    update_log[2][1] = str(found_rows)
    update_log[3][1] = str(new_rows)
    list_to_csv(update_log, 'update_log.csv')


def pd_to_csv_file(input_data, csv_name):
    input_data.to_csv(data_path + 'data/' + csv_name, header=True, index=False)


def import_local_data():
    # Read the CSV file
    col_names = ['id', 'Decision_Date', 'Employer', 'City_State', 'Case_Status', 'Job_Title', 'Wage_Offer']
    local_df = pd.read_csv(data_path + 'data/TW_PERM.csv', names=col_names, dtype=str, skiprows=1)
    # Convert DateTime
    data_cleaning.convert_datetime(local_df, 'Decision_Date')
    return local_df


def import_online_data():
    # Get new data
    online_df = download_data.download_data()
    # Convert DateTime
    data_cleaning.convert_datetime(online_df, 'Decision_Date')
    return online_df


def get_df_rows(data_name):
    return len(data_name.index)


def append_new_data(old_data_name, new_data_name):
    raw_data = old_data_name.append(new_data_name, ignore_index=True).drop_duplicates()
    return raw_data


def found_new_obs(old_data_name, raw_data_name):
    old_data_len = get_df_rows(old_data_name)
    raw_data_len = get_df_rows(raw_data_name)
    return str(raw_data_len - old_data_len)


def import_main():
    old_data = import_local_data()
    new_data = import_online_data()

    appended_data = append_new_data(old_data, new_data)
    found_new = found_new_obs(old_data, appended_data)

    # update local data
    logging_updates(get_df_rows(old_data), get_df_rows(new_data), found_new)
    pd_to_csv_file(appended_data, 'TW_PERM.csv')

    # Convert to equivalent annual salary
    data_cleaning.equivalent_annual_salary(appended_data, 'Wage_Offer')

    # Clean Case Status
    data_cleaning.clean_case_status(appended_data, 'Case_Status')

    # Separate State and City
    data_cleaning.separate_tate_city(appended_data, 'City_State')

    # Clean employer name
    data_cleaning.clean_employer_name(appended_data, 'Employer')

    # Add Area
    data_cleaning.add_area(appended_data, 'City_State')

    # NaN
    data_cleaning.clear_nan_value(appended_data)

    sorted_appended_data = appended_data.sort_values('Decision_Date', ascending=False)

    return sorted_appended_data
