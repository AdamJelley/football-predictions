# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import requests
import API_Functions
from API_Functions import BASE_URL, QUERYSTRING

leagues_df = dataiku.Dataset("Leagues_prepared_filtered").get_dataframe()

headers = API_Functions.getAPIRequestHeaders()

fixtures_df = pd.DataFrame()
for league_id in leagues_df['league_id']:
    df = API_Functions.getFixturesByLeague(league_id, BASE_URL, headers, QUERYSTRING)
    print(str(league_id) + ' done: ' + str(df.shape))
    fixtures_df = fixtures_df.append(df)

# Write recipe outputs
fixtures = dataiku.Dataset("Fixtures")
fixtures.write_with_schema(fixtures_df)