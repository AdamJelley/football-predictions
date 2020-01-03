# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import requests
import API_Functions
from API_Functions import BASE_URL, QUERYSTRING

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
fixtures_prepared = dataiku.Dataset("Fixtures_prepared")
fixtures_prepared_df = fixtures_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
headers = API_Functions.getAPIRequestHeaders()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
fixture_lineups = []
for fixture_id in fixtures_prepared_df['fixture_id']:
    fixture_lineup = API_Functions.getLineupsByFixture(fixture_id, BASE_URL, headers, QUERYSTRING)
    fixture_lineups.append(fixture_lineup)
fixture_lineups = pd.concat(fixture_lineups)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
fixtures_prepared_df_reduced = fixtures_prepared_df[['event_date', 'fixture_id',
        'homeTeam_team_id', 'homeTeam_team_name', 'awayTeam_team_id', 'awayTeam_team_name', 'league_name', 'goalsHomeTeam', 'goalsAwayTeam', 'statusShort']]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
fixture_lineups_enriched = fixtures_prepared_df_reduced.merge(fixture_lineups, how='inner', left_on = 'fixture_id', right_on='fixture_id')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
lineups_df = fixture_lineups_enriched

# Write recipe outputs
lineups = dataiku.Dataset("Lineups")
lineups.write_with_schema(lineups_df)