

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