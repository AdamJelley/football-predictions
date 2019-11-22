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