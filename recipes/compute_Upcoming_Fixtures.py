# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import requests
import API_Functions
from API_Functions import BASE_URL, QUERYSTRING

# Read recipe inputs
leagues_prepared_filtered = dataiku.Dataset("Leagues_prepared_filtered")
leagues_prepared_filtered_df = leagues_prepared_filtered.get_dataframe()

headers = API_Functions.getAPIRequestHeaders()

startDate = pd.to_datetime('today')
endDate = (pd.to_datetime('today') + pd.Timedelta('6 days'))
upcomingDates = list(pd.date_range(startDate, endDate).strftime('%Y-%m-%d'))

upcoming_Fixtures_df = pd.DataFrame()
for date in upcomingDates:
    df = API_Functions.getFixturesByDate(date, BASE_URL, headers, QUERYSTRING)
    print(str(date) + ' done: ' + str(df.shape))
    upcoming_Fixtures_df = upcoming_Fixtures_df.append(df)
    upcoming_Fixtures_df = upcoming_Fixtures_df[upcoming_Fixtures_df['league_id'].isin(leagues_prepared_filtered_df['league_id'])]

# Write recipe outputs
upcoming_Fixtures = dataiku.Dataset("Upcoming_Fixtures")
upcoming_Fixtures.write_with_schema(upcoming_Fixtures_df)