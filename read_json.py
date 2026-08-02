import json

with open("game.json") as file:
    game = json.load(file)

print(game["home_team"])
print(game["home_score"])
