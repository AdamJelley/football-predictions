# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import requests

leagues_df = dataiku.Dataset("Leagues_prepared_filtered").get_dataframe()

base_url = 'https://api-football-v1.p.rapidapi.com/v2/'

querystring = {"timezone":"Europe/London"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "6feb679189msh0e2593854adc7e5p1c15a8jsnbaa3c48b1a11"
    }

def getRemainingRequests(base_url, headers, querystring):
    status_url = base_url + '/seasons'
    response = requests.request("GET", status_url, headers=headers, params=querystring)
    remaining = int(response.headers['X-RateLimit-requests-Remaining'])
    return remaining

def getFixturesByLeague(league_id, base_url, headers, querystring):
    """Get fixtures dataframe for particular league id"""
    if getRemainingRequests(base_url, headers, querystring) > 0:
        fixtures_url = base_url + '/fixtures/league/' + str(league_id)
        fixtures_response = requests.request("GET", fixtures_url, headers=headers, params=querystring)
        fixtures_df = pd.DataFrame(fixtures_response.json()['api']['fixtures'])
    else:
        raise ValueError('No remaining requests. Try again tomorrow.')
    return fixtures_df

fixtures_df = pd.DataFrame()
for league_id in leagues_df['league_id']:
    df = getFixturesByLeague(league_id, base_url, headers, querystring)
    print(str(league_id) + ' done: ' + str(df.shape))
    fixtures_df = fixtures_df.append(df)

# Write recipe outputs
fixtures = dataiku.Dataset("Fixtures")
fixtures.write_with_schema(fixtures_df)