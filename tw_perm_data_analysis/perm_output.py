# __author__ = 'ktc312'
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import data_cleaning

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tw_perm_data_analysis/')


def update_summarize_main(input_data):
    summary = input_data.describe().head(1)
    approved_df = input_data.loc[input_data['Case_Status'].isin(['Certified-Expired', 'Certified'])]
    approved_summary = approved_df.describe().head(1)

    ny_df = approved_df.loc[input_data['Area'].isin(['New York Metro'])]
    ny_summary = ny_df.describe()
    ny_median = ny_df.median()
    ny_all = pd.concat([ny_summary, ny_median], axis=0)
    ny_all.to_csv(data_path + 'output/summarize_ny.csv')
    ny_count = ny_summary.head(1)

    ny_salary_1 = ny_df.loc[ny_df['Salary'] <= 20000].count().head(1)
    ny_salary_2 = ny_df.loc[ny_df['Salary'] >= 20001]
    ny_salary_2_3 = ny_salary_2.loc[ny_salary_2['Salary'] <= 30000].count().head(1)
    ny_salary_3 = ny_df.loc[ny_df['Salary'] >= 30001]
    ny_salary_3_4 = ny_salary_3.loc[ny_salary_3['Salary'] <= 40000].count().head(1)
    ny_salary_4 = ny_df.loc[ny_df['Salary'] >= 40001]
    ny_salary_4_5 = ny_salary_4.loc[ny_salary_4['Salary'] <= 50000].count().head(1)
    ny_salary_5 = ny_df.loc[ny_df['Salary'] >= 50001]
    ny_salary_5_6 = ny_salary_5.loc[ny_salary_5['Salary'] <= 60000].count().head(1)
    ny_salary_6 = ny_df.loc[ny_df['Salary'] >= 60001]
    ny_salary_6_7 = ny_salary_6.loc[ny_salary_6['Salary'] <= 70000].count().head(1)
    ny_salary_7 = ny_df.loc[ny_df['Salary'] >= 70001]
    ny_salary_7_8 = ny_salary_7.loc[ny_salary_7['Salary'] <= 80000].count().head(1)
    ny_salary_8 = ny_df.loc[ny_df['Salary'] >= 80001]
    ny_salary_8_9 = ny_salary_8.loc[ny_salary_8['Salary'] <= 90000].count().head(1)
    ny_salary_9 = ny_df.loc[ny_df['Salary'] >= 90001]
    ny_salary_9_10 = ny_salary_9.loc[ny_salary_9['Salary'] <= 100000].count().head(1)
    ny_salary_10 = ny_df.loc[ny_df['Salary'] >= 100001]
    ny_salary_10_11 = ny_salary_10.loc[ny_salary_10['Salary'] <= 110000].count().head(1)
    ny_salary_11 = ny_df.loc[ny_df['Salary'] >= 110001]
    ny_salary_11_12 = ny_salary_11.loc[ny_salary_11['Salary'] <= 120000].count().head(1)
    ny_salary_12 = ny_df.loc[ny_df['Salary'] >= 120001]
    ny_salary_12_13 = ny_salary_12.loc[ny_salary_12['Salary'] <= 130000].count().head(1)
    ny_salary_13 = ny_df.loc[ny_df['Salary'] >= 130001]
    ny_salary_13_14 = ny_salary_13.loc[ny_salary_13['Salary'] <= 140000].count().head(1)
    ny_salary_14 = ny_df.loc[ny_df['Salary'] >= 140001]
    ny_salary_14_15 = ny_salary_14.loc[ny_salary_14['Salary'] <= 150000].count().head(1)
    ny_salary_15 = ny_df.loc[ny_df['Salary'] >= 150001].count().head(1)
    ny_salary_all = pd.concat([ny_salary_1, ny_salary_2_3, ny_salary_3_4, ny_salary_4_5, ny_salary_5_6, ny_salary_6_7,
                               ny_salary_7_8, ny_salary_8_9, ny_salary_9_10, ny_salary_10_11, ny_salary_11_12,
                               ny_salary_12_13, ny_salary_13_14, ny_salary_14_15, ny_salary_15], axis=0)
    # print ny_salary_all
    item_list = ['< 20,000', '20,001 - 30,000', '30,001 - 40,000', '40,001 - 50,000', '50,001 - 60,000',
                 '60,001 - 70,000',
                 '70,001 - 80,000', '80,001 - 90,000', '90,001 - 100,000', '100,001 - 110,000', '110,001 - 120,000',
                 '120,001 - 130,000', '130,001 - 140,000', '140,001 - 150,000', '> 150,001']
    out_list = list()
    for i in ny_salary_all:
        short_list = list()
        short_list.append(item_list.pop(0))
        short_list.append(i)
        out_list.append(short_list)
    ny_salary_all = pd.DataFrame(out_list)
    ny_salary_all.to_csv(data_path + 'output/ny_salary_all.csv')

    top_ten_com = pd.crosstab(index=approved_df["Company"], columns="Count").sort_values('Count', ascending=False
                                                                                         ).head(10)
    top_ten_com.to_csv(data_path + 'output/top_ten_com.csv')
    top_ten_state = pd.crosstab(index=approved_df["State"], columns="Count").sort_values('Count', ascending=False
                                                                                         ).head(10)
    top_ten_state.to_csv(data_path + 'output/top_ten_state.csv')

    sorted_df = input_data.sort_values('Decision_Date', ascending=True)
    last_year_mon = list()
    last_year_mon.append(str(sorted_df.iloc[[-1]]['Decision_Date']).split('-')[0][4:])

    if int(str(sorted_df.iloc[[-1]]['Decision_Date']).split('-')[1]) < 10:
        last_year_mon.append(str(sorted_df.iloc[[-1]]['Decision_Date']).split('-')[1][1:])
    else:
        last_year_mon.append(str(sorted_df.iloc[[-1]]['Decision_Date']).split('-')[1])
    last_year_mon_df = pd.DataFrame(last_year_mon)

    summarize_main = pd.concat([summary, approved_summary, ny_count, last_year_mon_df], axis=0)
    summarize_main.to_csv(data_path + 'output/summarize_main.csv')

    last_year = int(str(sorted_df.iloc[[-1]]['Decision_Date']).split('-')[0][4:])
    yr = 2007
    all_yr_means = list()
    while yr <= last_year-1:
        yr_df = approved_df.loc[approved_df['Decision_Date'].dt.year == yr]
        the_list = list()
        the_list.append(str(yr))
        yr_mean = yr_df.mean()
        yr_median = yr_df.median()
        for i in yr_mean:
            the_list.append(round(i, 2))
        for i in yr_median:
            the_list.append(round(i, 2))
        all_yr_means.append(the_list)
        yr += 1
    f = open(data_path + 'output/all_yr_means.csv', "w")
    f.write("\n".join(map(lambda x: str(x), all_yr_means)))
    f.close()

    remove_rare_state = data_cleaning.remove_rare_case(approved_df, 'State', 0.15)
    ave_by_state = remove_rare_state.groupby(['State']).mean().sort_values('Salary', ascending=False).head(10)
    ave_by_state.rename(columns={'Salary': 'means'}, inplace=True)
    top_states = remove_rare_state.loc[remove_rare_state['State'].isin(list(ave_by_state.index))]
    median_by_state = top_states.groupby(['State']).median().sort_values('Salary', ascending=False).head(10)
    median_by_state.rename(columns={'Salary': 'median'}, inplace=True)
    ave_median_by_state = pd.merge(ave_by_state, median_by_state, left_index=True, right_index=True)
    sorted_ave_median_by_state = ave_median_by_state.sort_values('means', ascending=False)
    sorted_ave_median_by_state.to_csv(data_path + 'output/ave_by_state.csv')

    top_median_state = remove_rare_state.groupby(['State']).median().sort_values('Salary', ascending=False).head(1)
    top_median_state.to_csv(data_path + 'output/top_median_state.csv')


def plot_and_sum(input_data, year, area):
    # Index Base Data
    if year == area == 'ALL':
        update_summarize_main(input_data)
    # ALL other statistics
    try:
        # if year == 'ALL':
        #     if area == 'ALL':
        #         title = 'Salary Distribution of all years in US'
        #     else:
        #         title = 'Salary Distribution of all years in %s' % area
        # else:
        #     if area == 'ALL':
        #         title = 'Salary Distribution of year %s in US' % str(year)
        #     else:
        #         title = "Salary Distribution of year %s in " % str(year)
        #         title = title + area
        # input_data.plot.hist(alpha=0.5, bins=100, title=title)
        # plt.savefig(data_path + 'output/hist_' + area + str(year) + '.png')
        # plt.close()
        # summary
        summary = input_data.describe()
        # top 10 states
        top_10_state = pd.crosstab(index=input_data["State"], columns="Count"
                                   ).sort_values('Count', ascending=False).head(10)
        ave_by_state = input_data.groupby(['State']).mean().sort_values('Salary', ascending=False).head(10)
        # top 10 companies
        top_10_com = pd.crosstab(index=input_data["Company"], columns="Count"
                                 ).sort_values('Count', ascending=False).head(10)
        ave_by_com = input_data.groupby(['Company']).mean().sort_values('Salary', ascending=False).head(10)
        result = pd.concat([summary, top_10_state, ave_by_state, top_10_com, ave_by_com], axis=0)
        result.to_csv(data_path + 'output/summarize_' + area + str(year) + '.csv')
    except:
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e


def gen_sum(input_data, year='ALL', area='ALL'):
    if year == 'ALL':
        if area == 'ALL':
            plot_and_sum(input_data, year, area)
        else:
            area_df = input_data.loc[input_data['Area'] == area]
            plot_and_sum(area_df, year, area)
    else:
        if area == 'ALL':
            year_df = input_data.loc[input_data['Decision_Date'].dt.year == year]
            plot_and_sum(year_df, year, area)
        else:
            area_df = input_data.loc[input_data['Area'] == area]
            year_df = area_df.loc[area_df['Decision_Date'].dt.year == year]
            plot_and_sum(year_df, year, area)
