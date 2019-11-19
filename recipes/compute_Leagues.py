# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import requests

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
base_url = 'https://api-football-v1.p.rapidapi.com/v2/'

querystring = {"timezone":"Europe/London"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "6feb679189msh0e2593854adc7e5p1c15a8jsnbaa3c48b1a11"
    }

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
leagues_url = base_url + '/leagues'
leagues_response = requests.request("GET", leagues_url, headers=headers, params=querystring)
leagues_df = pd.DataFrame(leagues_response.json()['api']['leagues'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
leagues = dataiku.Dataset("Leagues")
leagues.write_with_schema(leagues_df)