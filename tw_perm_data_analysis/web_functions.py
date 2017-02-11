# __author__ = 'ktc312'
import os

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tw_perm_data_analysis/')


def read_csv_to_list(file_name):
    with open(data_path + file_name) as f:
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


def read_summarize_main():
    with open(data_path + 'output/summarize_main.csv') as f:
        the_list = [line.rstrip('\n') for line in f]
    list_of_lists = list()
    for i in the_list:
        the_list = i.split(',')
        list_of_lists.append(the_list)
    total_perm = list_of_lists[1][2]
    approved_perm = list_of_lists[2][2]
    ny_perm = list_of_lists[3][2]
    end_year = list_of_lists[4][1]
    end_mon = list_of_lists[5][1]
    return total_perm, approved_perm, ny_perm, end_year, end_mon


def read_summarize_ny():
    with open(data_path + 'output/summarize_ny.csv') as f:
        the_list = [line.rstrip('\n') for line in f]
    list_of_lists = list()
    for i in the_list:
        the_list = i.split(',')
        list_of_lists.append(the_list)
    ny_mean = str(round(float(list_of_lists[2][2]), 2))
    ny_std = str(round(float(list_of_lists[3][2]), 2))
    ny_median = str(round(float(list_of_lists[9][1]), 2))
    ny_min = list_of_lists[4][2].split('.')[0]
    ny_max = list_of_lists[8][2].split('.')[0]
    return ny_mean, ny_std, ny_median, ny_min, ny_max


def read_top_ten_com():
    summarize_main = read_summarize_main()
    approved_perm = int(summarize_main[1].split('.')[0])
    with open(data_path + 'output/top_ten_com.csv') as f:
        the_list = [line.rstrip('\n') for line in f]
    list_of_lists = list()
    for i in the_list:
        the_list = i.split(',')
        list_of_lists.append(the_list)
    list_of_lists.pop(0)
    final_list = list()
    for i in list_of_lists:
        i.append(str(round((float(i[1])/approved_perm), 4)*100)+"%")
        final_list.append(i)
    return final_list


def read_top_ten_state():
    summarize_main = read_summarize_main()
    approved_perm = int(summarize_main[1].split('.')[0])
    with open(data_path + 'output/top_ten_state.csv') as f:
        the_list = [line.rstrip('\n') for line in f]
    list_of_lists = list()
    for i in the_list:
        the_list = i.split(',')
        list_of_lists.append(the_list)
    list_of_lists.pop(0)
    final_list = list()
    for i in list_of_lists:
        i.append(str(round((float(i[1])/approved_perm), 4)*100)+"%")
        final_list.append(i)
    with open(data_path + 'data/State_list.csv') as f:
        the_list = [line.rstrip('\n') for line in f]
        state_list = list()
        for i in the_list:
            state_list.append(i)
    out_list = list()
    for i in final_list:
        new_list = list()
        for x in state_list:
            if i[0] == x[:2]:
                new_list.append(x[3:])
                new_list.append(i[1])
                new_list.append(i[2])
        out_list.append(new_list)
    return out_list


def read_ny_salary_all():
    with open(data_path + 'output/ny_salary_all.csv') as f:
        the_list = [line.rstrip('\n') for line in f]
    the_list.pop(0)
    out_list = list()
    for i in the_list:
        short_list = list()
        short_list.append(i.split('"')[1])
        short_list.append(i.split('"')[2][1:])
        out_list.append(short_list)
    return out_list


def read_all_yr_means():
    with open(data_path + 'output/all_yr_means.csv') as f:
        the_list = [line.rstrip('\n') for line in f]
    out_list = list()
    for i in the_list:
        short_list = list()
        short_list.append(i.split(',')[0][2:-1])
        short_list.append(i.split(',')[1][1:])
        short_list.append(i.split(',')[2][1:-1])
        out_list.append(short_list)
    return out_list


def read_top_10_state_mean():
    with open(data_path + 'output/ave_by_state.csv') as f:
        the_list = [line.rstrip('\n') for line in f]
    the_list.pop(0)
    with open(data_path + 'data/State_list.csv') as f:
        the_s_list = [line.rstrip('\n') for line in f]
        state_list = list()
        for i in the_s_list:
            state_list.append(i)
    out_list = list()
    for i in the_list:
        new_list = list()
        for x in state_list:
            if i.split(',')[0] == x[:2]:
                new_list.append(x[3:])
                new_list.append(str(round(float(i.split(',')[1]), 2)))
                new_list.append(i.split(',')[2])
        out_list.append(new_list)
    return out_list


def read_top_median_state():
    with open(data_path + 'output/top_median_state.csv') as f:
        the_list = [line.rstrip('\n') for line in f]
    the_list.pop(0)
    with open(data_path + 'data/State_list.csv') as f:
        the_s_list = [line.rstrip('\n') for line in f]
        state_list = list()
        for i in the_s_list:
            state_list.append(i)
    out_list = list()
    for i in the_list:
        for x in state_list:
            if i.split(',')[0] == x[:2]:
                out_list.append(x[3:])
                out_list.append(i.split(',')[1])
    return out_list
