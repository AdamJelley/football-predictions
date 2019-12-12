import dataiku
import pandas as pd
from flask import request


# Example:
# As the Python webapp backend is a Flask app, refer to the Flask
# documentation for more information about how to adapt this
# example to your needs.
# From JavaScript, you can access the defined endpoints using
# getWebAppBackendUrl('first_api_call')

@app.route('/predictions')
def get_predictions():
    max_rows = request.args.get('max_rows') if 'max_rows' in request.args else 100
    mydataset = dataiku.Dataset("Upcoming_Fixtures_EloFeatures_scored")
    df = mydataset.get_dataframe()
    df = df[['event_date', 'homeTeam_team_name', 'awayTeam_team_name', 'league_name', 'venue', 'proba_Home', 'proba_Away', 'proba_Draw', 'prediction']]
    df = df.sort_values('event_date', ascending=True).head(max_rows)
    df = df.rename(columns={"event_date":"Match Start", "homeTeam_team_name": "Home Team", "awayTeam_team_name": "Away Team", "league_name":"League", "venue":"Venue", "proba_Home":"Prob Home Win", "proba_Away":"Prob Away Win", "proba_Draw":"Prob Draw", "prediction":"Prediction"})
    data = df.to_html(index=False)
    return json.dumps({"status": "ok", "data": data})

@app.route('/history')
def get_history():
    max_rows = request.args.get('max_rows') if 'max_rows' in request.args else 100
    mydataset = dataiku.Dataset("Historical_Fixtures_Evaluated")
    df = mydataset.get_dataframe()
    df = df[['event_date', 'homeTeam_team_name', 'awayTeam_team_name', 'league_name', 'venue', 'proba_Home', 'proba_Away', 'proba_Draw', 'prediction', 'score_fulltime', 'prediction_correct']]
    df = df.sort_values('event_date', ascending=False).head(max_rows)
    df = df.rename(columns={"event_date":"Match Start", "homeTeam_team_name": "Home Team", "awayTeam_team_name": "Away Team", "league_name":"League", "venue":"Venue", "proba_Home":"Prob Home Win", "proba_Away":"Prob Away Win", "proba_Draw":"Prob Draw", "prediction":"Prediction", 'score_fulltime':"Score", 'prediction_correct':"Prediction Correct"})
    data = df.to_html(index=False, justify='left')
    return json.dumps({"status": "ok", "data": data})

@app.route('/rankings')
def get_rankings():
    max_rows = request.args.get('max_rows') if 'max_rows' in request.args else 100
    mydataset = dataiku.Dataset("Latest_Team_Elo_Ranks")
    df = mydataset.get_dataframe()
    df = df[['teamName', 'Elo_rank']]
    df.Elo_rank = df.Elo_rank.astype('int')
    df = df.sort_values('Elo_rank', ascending=False).head(max_rows)
    df = df.rename(columns={'teamName':"Team Name", 'Elo_rank':"Elo Rank"})
    data = df.to_html(index=False)
    return json.dumps({"status": "ok", "data": data})