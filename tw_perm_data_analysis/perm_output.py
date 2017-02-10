# __author__ = 'ktc312'
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

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
