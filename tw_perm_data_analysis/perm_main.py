# __author__ = 'ktc312'
from import_data import import_main
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tw_perm_data_analysis/')


def gen_sum(input_data, year='ALL', area='ALL'):
    if year == area == 'ALL':
        # histogram
        input_data.plot.hist(alpha=0.5, bins=100)
        plt.savefig(data_path + 'output/hist_' + year + '.png')
        # summary
        summary = tw_perm_df.describe()
        # top 10 states
        top_10_state = pd.crosstab(index=tw_perm_df["State"], columns="Count"
                                   ).sort_values('Count', ascending=False).head(10)
        ave_by_state = tw_perm_df.groupby(['State']).mean().sort_values('Salary', ascending=False).head(10)
        # top 10 companies
        top_10_com = pd.crosstab(index=tw_perm_df["Company"], columns="Count"
                                 ).sort_values('Count', ascending=False).head(10)
        ave_by_com = tw_perm_df.groupby(['Company']).mean().sort_values('Salary', ascending=False).head(10)
        result = pd.concat([summary, top_10_state, ave_by_state, top_10_com, ave_by_com], axis=0)
        result.to_csv(data_path + 'output/summarize_' + year + '.csv')

    else:
        # TODO: loop function to loop through all years and areas
        pass

tw_perm_df = import_main()
gen_sum(tw_perm_df)

# tw_perm_df.plot.density()

# print tw_perm_df.isnull().sum()
# print tw_perm_df.loc[tw_perm_df['Salary'] < 16000]
# com_tab = pd.crosstab(index=tw_perm_df["Employer"], columns="Count")
