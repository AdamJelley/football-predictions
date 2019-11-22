# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import requests
import API_Functions 

leagues_df = dataiku.Dataset("Leagues_prepared_filtered").get_dataframe()

import dataiku

BASE_URL = 'https://api-football-v1.p.rapidapi.com/v2/'

QUERYSTRING = {"timezone":"Europe/London"}

def getAPIRequestHeaders():
    client = dataiku.api_client()
    auth_info = client.get_auth_info(with_secrets=True)

    x-rapidapi-key = None
    for secret in auth_info["secrets"]:
        if secret["key"] == "x-rapidapi-key":
            x-rapidapi-key = secret["value"]
            break
    if not x-rapidapi-key:
            raise Exception("x-rapidapi-key not found")

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': x-rapidapi-key
        }
        
    return headers

headers = API_Functions.getAPIRequestHeaders()

fixtures_df = pd.DataFrame()
for league_id in leagues_df['league_id']:
    df = getFixturesByLeague(league_id, BASE_URL, headers, QUERYSTRING)
    print(str(league_id) + ' done: ' + str(df.shape))
    fixtures_df = fixtures_df.append(df)

# Write recipe outputs
fixtures = dataiku.Dataset("Fixtures")
fixtures.write_with_schema(fixtures_df)