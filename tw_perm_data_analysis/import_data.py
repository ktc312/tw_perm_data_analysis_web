# __author__ = 'ktc312'
#  -*- coding: utf-8 -*-
# coding: utf-8
import pandas as pd
import os
import data_cleaning
import download_data

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tw_perm_data_analysis/')

# Read the CSV file
col_names = ['id', 'Decision_Date', 'Employer', 'City_State', 'Case_Status', 'Job_Title', 'Wage_Offer']
old_df = pd.read_csv(data_path + 'data/TW_PERM.csv', names=col_names, dtype=str, skiprows=1)

# Get new data
new_df = download_data.download_data()

# Convert DateTime
data_cleaning.convert_datetime(old_df, 'Decision_Date')
data_cleaning.convert_datetime(new_df, 'Decision_Date')

# Add new rows into data
raw_df = old_df.append(new_df, ignore_index=True).drop_duplicates()
found_new_obs = str(len(raw_df.index) - len(old_df.index))

# Convert to equivalent annual salary
data_cleaning.equivalent_annual_salary(raw_df, 'Wage_Offer')

# Clean Case Status
data_cleaning.clean_case_status(raw_df, 'Case_Status')

# Separate State and City
data_cleaning.separate_tate_city(raw_df, 'City_State')

# Add Area
data_cleaning.add_area(raw_df, 'City_State')

tw_perm_df = raw_df.sort_values('Decision_Date', ascending=False)


# TODO: func to update the csv file in database
def update_csv_file():
    pass

print 'Found ' + found_new_obs + ' new observations today!'
print 'Here are some sample: '

area_tab = pd.crosstab(index=tw_perm_df["Area"], columns="Count")
print area_tab
# com_tab = pd.crosstab(index=tw_perm_df["Employer"], columns="Count")
# print com_tab
