import json 

def trigger_led(team_name):
    print(f"LED effect triggered for {team_name}")

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

if current_game["home_score"] > previous_game["home_score"]:
    print(f'{current_game["home_team"]} scored')
    trigger_led(current_game["home_team"]) 


