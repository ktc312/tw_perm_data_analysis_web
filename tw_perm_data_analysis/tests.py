from django.test import TestCase

# Create your tests here.
import download_data
import data_cleaning
import pandas as pd

online_df = download_data.download_data()
print online_df.head(5)
online_df['Decision_Date'] = pd.to_datetime(online_df['Decision_Date'])

print online_df.head(5)
