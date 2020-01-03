# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import requests
import API_Functions
from API_Functions import BASE_URL, QUERYSTRING

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
headers = API_Functions.getAPIRequestHeaders()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
leagues_df = API_Functions.getAvailableLeagues(BASE_URL, headers, QUERYSTRING)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
leagues = dataiku.Dataset("Leagues")
leagues.write_with_schema(leagues_df)