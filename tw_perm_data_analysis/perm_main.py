# __author__ = 'ktc312'
from import_data import import_main
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tw_perm_data_analysis/')

tw_perm_df = import_main()

# tw_perm_df.hist()
tw_perm_df.plot.hist(alpha=0.5, bins=20)
plt.savefig(data_path + 'data/test_figure.png')


# print tw_perm_df.describe()

# state_tab = pd.crosstab(index=tw_perm_df["State"], columns="Count").sort_values('Count', ascending=False)
# print state_tab.head(10)
# ave_by_state = tw_perm_df.groupby(['State']).mean().sort_values('Salary', ascending=False)
# print ave_by_state.head(10)

# com_tab = pd.crosstab(index=tw_perm_df["Company"], columns="Count").sort_values('Count', ascending=False)
# print com_tab.head(10)
# ave_by_com = tw_perm_df.groupby(['Company']).mean().sort_values('Salary', ascending=False)
# print ave_by_com.head(10)


# area_tab = pd.crosstab(index=tw_perm_df["Area"], columns="Count")
# status_tab = pd.crosstab(index=tw_perm_df["Case_Status"], columns="Count")
# print area_tab
# print status_tab
# print tw_perm_df.head(1)
# print tw_perm_df.isnull().sum()
# print tw_perm_df.loc[tw_perm_df['Salary'] < 16000]
# com_tab = pd.crosstab(index=tw_perm_df["Employer"], columns="Count")
# print com_tab

