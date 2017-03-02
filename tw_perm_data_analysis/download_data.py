# __author__ = 'ktc312'
#  -*- coding: utf-8 -*-
# coding: utf-8
import urllib2 as ul
from bs4 import BeautifulSoup
import csv
import os
import pandas as pd
import time
import data_cleaning

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tw_perm_data_analysis/')

# Construct the visadoor search url
base_url = str('http://visadoor.com/greencards/index?country=Taiwan&submit=Search')


def raw_data_rows_to_csv(list_data, file_name):
    with open(data_path + "data/" + file_name, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(list_data)


# get last_year
def get_last_year():
    col_names = ['id', 'Decision_Date', 'Employer', 'City_State', 'Case_Status', 'Job_Title', 'Wage_Offer']
    tw_perm_df = pd.read_csv(data_path + 'data/TW_PERM.csv', names=col_names, dtype=str, skiprows=1)
    data_cleaning.convert_datetime(tw_perm_df, 'Decision_Date')
    sorted_df = tw_perm_df.sort_values('Decision_Date', ascending=True)
    return str(sorted_df.iloc[[-1]]['Decision_Date']).split('-')[0][-4:]

get_last_year()

# get cases found
def get_cases_found(last_year):
    cases_found_in_page = 0
    test_search_term = '&year=' + last_year
    soup = BeautifulSoup(ul.urlopen(base_url + test_search_term, data=None, timeout=5), "html.parser")
    cases_found_class = soup.findAll("div", {"class": "col-sm-5"})
    for div in cases_found_class:
        cases_found_in_page = int(str(div).split('<h4>')[1].split(' ')[3])
    return cases_found_in_page


# get page count
def get_page_count(cases):
    if cases <= 1000:
        count = 1
    else:
        count = (cases/1000) + 1
    return count


# get data
def scrape_data(last_year, page_count):
    i = 0
    encode_raw_data = []
    while i < page_count:
        search_term = '&year=' + last_year + '&page=' + str(i+1)
        soup = BeautifulSoup(ul.urlopen(base_url + search_term, data=None, timeout=5), "html.parser")
        # get data table
        raw_data = []
        table = soup.find('table', attrs={'class': 'table table-bordered table-striped table-hover'})
        rows = table.findAll('tr')
        for row in rows:
            cols = row.findAll('td')
            cols = [ele.text.strip() for ele in cols]
            for col in cols:
                raw_data.append(col)

        for u_item in raw_data:
            encode_raw_data.append(u_item.encode('UTF8'))
        time.sleep(5)
        i += 1

    i = 0
    encode_raw_data_rows = []
    while i < len(encode_raw_data):
        encode_raw_data_rows.append(encode_raw_data[i:i+7])
        i += 7
    raw_data_rows_to_csv(encode_raw_data_rows, 'temp_new_data.csv')

    col_names = ['id', 'Decision_Date', 'Employer', 'City_State', 'Case_Status', 'Job_Title', 'Wage_Offer']
    new_df = pd.read_csv(data_path + 'data/temp_new_data.csv', names=col_names, dtype=str, skiprows=1)

    return new_df


# get the latest data
def download_data():
    last_yr = get_last_year()
    pages = get_page_count(get_cases_found(last_yr))
    return scrape_data(last_yr, pages)
