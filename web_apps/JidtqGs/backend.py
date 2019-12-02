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
    max_rows = request.args.get('max_rows') if 'max_rows' in request.args else 500
    mydataset = dataiku.Dataset("Upcoming_Fixtures_EloFeatures_scored")
    df = mydataset.get_dataframe(sampling='head', limit=max_rows)
    df = df[['event_date', 'homeTeam_team_name', 'awayTeam_team_name', 'league_name', 'venue', 'proba_Home', 'proba_Away', 'proba_Draw', 'prediction']]
    df = df.sort_values('event_date', ascending=True)
    data = df.to_html(index=False)
    return json.dumps({"status": "ok", "data": data})
