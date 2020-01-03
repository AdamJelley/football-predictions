import dataiku
import pandas as pd, numpy as np
import requests

BASE_URL = 'https://api-football-v1.p.rapidapi.com/v2/'

QUERYSTRING = {"timezone":"Europe/London"}

def getAPIRequestHeaders():
    client = dataiku.api_client()
    auth_info = client.get_auth_info(with_secrets=True)

    x_rapidapi_key = None
    for secret in auth_info["secrets"]:
        if secret["key"] == "x-rapidapi-key":
            x_rapidapi_key = secret["value"]
            break
    if not x_rapidapi_key:
            raise Exception("x-rapidapi-key not found")

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
        }
        
    return headers

def testRemainingRequests(base_url, headers, querystring):
    """Test remaining requests: fail if no requests remaining this month and give warning if < 100."""
    status_url = base_url + '/seasons'
    response = requests.request("GET", status_url, headers=headers, params=querystring)
    remaining = int(response.headers['X-RateLimit-requests-Remaining'])
    if remaining <= 0:
        raise ValueError('No remaining requests. Try again tomorrow.')
    elif remaining < 100:
        print('Warning: Only ' + str(remaining) + ' Requests Remaining')
    return 1

def getAvailableLeagues(base_url, headers, querystring):
    """Get league coverage from Football API"""
    testRemainingRequests(base_url, headers, querystring)
    leagues_url = BASE_URL + '/leagues'
    leagues_response = requests.request("GET", leagues_url, headers=headers, params=QUERYSTRING)
    leagues_df = pd.DataFrame(leagues_response.json()['api']['leagues'])
    return leagues_df

def getFixturesByLeague(league_id, base_url, headers, querystring):
    """Get fixtures dataframe for particular league id"""
    testRemainingRequests(base_url, headers, querystring)
    
    fixtures_url = base_url + '/fixtures/league/' + str(league_id)
    fixtures_response = requests.request("GET", fixtures_url, headers=headers, params=querystring)
    fixtures_df = pd.DataFrame(fixtures_response.json()['api']['fixtures'])

    return fixtures_df

def getFixturesByDate(date, base_url, headers, querystring):
    """Get fixtures dataframe for particular league id for a particular date"""
    testRemainingRequests(base_url, headers, querystring)
    
    date_fixtures_url = base_url + '/fixtures/date/' + str(date)
    date_fixtures_response = requests.request("GET", date_fixtures_url, headers=headers, params=querystring)
    date_fixtures_df = pd.DataFrame(date_fixtures_response.json()['api']['fixtures'])

    return date_fixtures_df