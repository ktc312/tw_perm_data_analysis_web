# __author__ = 'ktc312'
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tw_perm_data_analysis/')


def plot_and_sum(input_data, year, area):
    # histogram
    try:
        if year == 'ALL':
            if area == 'ALL':
                title = 'Salary Distribution of all years in US'
            else:
                title = 'Salary Distribution of all years in %s' % area
        else:
            if area == 'ALL':
                title = 'Salary Distribution of year %s in US' % str(year)
            else:
                title = "Salary Distribution of year %s in " % str(year)
                title = title + area
        input_data.plot.hist(alpha=0.5, bins=100, title=title)
        plt.savefig(data_path + 'output/hist_' + area + str(year) + '.png')
        plt.close()
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
