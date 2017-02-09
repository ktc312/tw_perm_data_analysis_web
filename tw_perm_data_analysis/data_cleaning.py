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
            annual_salary.append(wage * 2080)
        elif keyword in ('mth', 'month'):
            annual_salary.append(wage * 12)
        elif keyword in ('week', 'wk'):
            annual_salary.append(wage * 52)
        elif keyword == 'bi':
            annual_salary.append(wage * 26)
        elif float(input_wage_str[:-1]) <= 100:
            annual_salary.append(float(input_wage_str[:-1]) * 2080)
        else:
            annual_salary.append(float(input_wage_str[:-1]))

    input_data['Salary'] = np.asarray(annual_salary)
    input_data.drop(input_wage, axis=1, inplace=True)


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

    state = ['Missing' if v is '' else v for v in state]
    input_data['City'] = np.asarray(city)
    input_data['State'] = np.asarray(state)


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
                area.append('Missing')
        # TODO: add Bay Area cities list
        elif state == 'CA':
            if city in bay_cities:
                area.append('Bay Area')
            else:
                area.append('Missing')
        else:
            area.append('Missing')
    input_data['Area'] = np.asarray(area)
