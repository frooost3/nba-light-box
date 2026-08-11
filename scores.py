import json 

TEAM_COLOURS = {
    "Toronto Raptors": (206, 17, 65),
    "Boston Celtics": (0, 122, 51),
}

def trigger_led(team_name):
    colour = TEAM_COLOURS.get(team_name, (255, 255, 255))
    print(f"LED effect triggered for {team_name}")
    print(f"RGB colour: {colour}")

def check_score_change(previous_game, current_game):
    if current_game["home_score"] > previous_game["home_score"]:
        team = current_game["home_team"]
        print(f"{team} scored")
        trigger_led(team)

with open("game.json") as file:
    game = json.load(file)

print(f'{game["away_team"]} at {game["home_team"]}')
print (f'{game["away_score"]} - {game["home_score"]}')

if game["home_score"] > game["away_score"]:
    print(f'{game["home_team"]} is winning')
elif game["away_score"] > game["home_score"]:
    print(f'{game["away_team"]} is winning')
else:
    print("The game is tied")


previous_game = {
    "home_team": "Toronto Raptors",
    "home_score": 98
}

current_game = {
    "home_team": "Toronto Raptors",
    "home_score": 100
}

check_score_change(previous_game, current_game)
