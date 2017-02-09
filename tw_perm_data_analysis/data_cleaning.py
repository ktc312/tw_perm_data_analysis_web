# __author__ = 'ktc312'
import pandas as pd
import numpy as np
import os

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tw_perm_data_analysis/')

# Read the CSV file (cities)
ny_cities_df = pd.read_csv(data_path + 'data/NY_cities.csv', names='c', dtype=str)
ny_cities = []
for x in ny_cities_df['c']:
    ny_cities.append(x)
bay_cities_df = pd.read_csv(data_path + 'data/Bay_Area_cities.csv', names='city', dtype=str)
bay_cities = []
for x in bay_cities_df['c']:
    bay_cities.append(x)


# Convert DateTime
def convert_datetime(input_data, input_date):
    input_data[input_date] = pd.to_datetime(input_data[input_date])


# Convert to equivalent annual salary
def equivalent_annual_salary(input_data, input_wage):
    annual_salary = []
    for input_wage_str in input_data[input_wage]:
        wage = float(input_wage_str.split('/')[0].replace(",", ""))
        keyword = input_wage_str.split('/')[1].lower()
        if keyword in ('year', 'yr'):
            annual_salary.append(wage)
        elif keyword in ('hour', 'hr'):
            if wage < 1000:
                annual_salary.append(wage * 2080)
            else:
                annual_salary.append(wage)
        elif keyword in ('mth', 'month'):
            if wage < 100000:
                annual_salary.append(wage * 12)
            else:
                annual_salary.append(wage)
        elif keyword in ('week', 'wk'):
            if wage < 90000:
                annual_salary.append(wage * 52)
            else:
                annual_salary.append(wage)
        elif keyword == 'bi':
            annual_salary.append(wage * 26)
        elif float(input_wage_str[:-1]) <= 100:
            annual_salary.append(float(input_wage_str[:-1]) * 2080)
        else:
            annual_salary.append(float(input_wage_str[:-1]))

    input_data['Salary'] = np.asarray(annual_salary)
    input_data.drop(input_wage, axis=1, inplace=True)
    # remove outliers
    input_data.ix[input_data.Salary > 500000, 'Salary'] = '-999'


# Clean Case Status
def clean_case_status(input_data, input_status):
    input_data[input_status] = np.where(input_data[input_status] == 'Certified-expired',
                                        'Certified-Expired', input_data[input_status])


# Separate State and City
def separate_tate_city(input_data, input_region):
    city = []
    state = []
    for s_c in input_data[input_region]:

        if len(s_c.split(',')[1]) > 3:
            city.append(s_c.split(',')[0])
            state.append(s_c.split(',')[1][1:3].upper())
        else:
            city.append(s_c.split(',')[0])
            state.append(s_c.split(',')[1][1:3].upper())

    state = ['-999' if v is '' else v for v in state]
    input_data['City'] = np.asarray(city)
    input_data['State'] = np.asarray(state)


# Clean employer name
def clean_employer_name(input_data, input_employer):
    com_list = []
    com_list_2 = []
    for employer in input_data[input_employer]:
        com_list.append(employer.replace(',', ''))
    for com in com_list:
        com_list_2.append(com.replace('!', ''))

    input_data['Company'] = np.asarray(com_list_2)
    input_data.drop(input_employer, axis=1, inplace=True)


# Add Area
def add_area(input_data, input_region):
    area = []
    for s_c in input_data[input_region]:
        city = s_c.split(',')[0].upper()
        state = s_c.split(',')[1][1:3].upper()
        if state in ('NY', 'NJ', 'CT'):
            if city in ny_cities:
                area.append('New York Metro')
            else:
                area.append('-999')
        elif state == 'CA':
            if city in bay_cities:
                area.append('Bay Area')
            else:
                area.append('-999')
        else:
            area.append('-999')
    input_data['Area'] = np.asarray(area)


# NaN
def clear_nan_value(input_data):
    input_data['State'] = input_data['State'].replace({'-999': np.nan})
    input_data['Salary'] = input_data['Salary'].replace({'-999': np.nan})
    input_data['Area'] = input_data['Area'].replace({'-999': np.nan})
