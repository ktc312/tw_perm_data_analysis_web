# __author__ = 'ktc312'
from import_data import import_main
import pandas as pd

tw_perm_df = import_main()

# TODO: first output, Salary Distribution by Area
area_tab = pd.crosstab(index=tw_perm_df["Area"], columns="Count")
print area_tab

# com_tab = pd.crosstab(index=tw_perm_df["Employer"], columns="Count")
# print com_tab

