import requests

URL = "https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard"

data = requests.get(URL).json()

event = data["events"][0]
competitors = event["competitions"][0]["competitors"]

current_game = {}

for team in competitors:
    if team["homeAway"] == "home":
        current_game["home_team"] = team["team"]["displayName"]
        current_game["home_score"] = int(team["score"])

    else:
        current_game["away_team"] = team["team"]["displayName"]
        current_game["away_score"] = int(team["score"])

print (current_game)
