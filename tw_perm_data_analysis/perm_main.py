# __author__ = 'ktc312'
from import_data import import_main
import pandas as pd
import data_cleaning
import perm_output
import datetime
import os

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tw_perm_data_analysis/')


def update_all_outcome():
    years_list = ['ALL']
    areas_list = ['ALL', 'New York Metro', 'Bay Area']
    start_yr = 2008
    current_yr = datetime.datetime.now().year
    while start_yr <= current_yr:
        years_list.append(start_yr)
        start_yr += 1
    imported_data = import_main()
    for year in years_list:
        for area in areas_list:
            perm_output.gen_sum(imported_data, year, area)
    print 'Done updating'


def test_locally():
    col_names = ['id', 'Decision_Date', 'Employer', 'City_State', 'Case_Status', 'Job_Title', 'Wage_Offer']
    local_df = pd.read_csv(data_path + 'data/TW_PERM.csv', names=col_names, dtype=str, skiprows=1)
    data_cleaning.convert_datetime(local_df, 'Decision_Date')
    data_cleaning.equivalent_annual_salary(local_df, 'Wage_Offer')
    data_cleaning.clean_case_status(local_df, 'Case_Status')
    data_cleaning.separate_tate_city(local_df, 'City_State')
    data_cleaning.clean_employer_name(local_df, 'Employer')
    data_cleaning.add_area(local_df, 'City_State')
    data_cleaning.clear_nan_value(local_df)
    sorted_local_df = local_df.sort_values('Decision_Date', ascending=False)
    return sorted_local_df

# update_all_outcome()

tw_perm_df = test_locally()

# tw_perm_df.plot.density()
# print tw_perm_df.isnull().sum()
# print tw_perm_df.loc[tw_perm_df['Salary'] < 16000]
# com_tab = pd.crosstab(index=tw_perm_df["Employer"], columns="Count")
