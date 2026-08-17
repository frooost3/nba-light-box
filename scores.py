import json
import requests
import time
import board
import adafruit_pixelbuf 
from adafruit_raspberry_pi5_neopixel_write import neopixel_write

TEAM_COLOURS = {
    "Toronto Raptors": (206, 17, 65),
    "Boston Celtics": (0, 122, 51),
}

class Pi5Pixelbuf(adafruit_pixelbuf.PixelBuf):
    def __init__(self, pin, size, **kwargs):
        self._pin = pin
        super().__init__(size=size, **kwargs)

    def _transmit(self, buf):
        neopixel_write(self._pin, buf)

NEOPIXEL = board.D18
NUM_PIXELS = 60

pixels = Pi5Pixelbuf(
    NEOPIXEL,
    NUM_PIXELS,
    auto_write=True,
    byteorder="GRB"
)

def trigger_led(team_name):
    colour = TEAM_COLOURS.get(team_name, (255, 255, 255))

    print(f"LED effect triggered for {team_name}")
    print(f"RGB colour: {colour}")

    pixels.fill(colour)
    time.sleep(2)
    pixels.fill((0, 0, 0))

def check_score_change(previous_game, current_game):
    if current_game["home_score"] > previous_game["home_score"]:
        team = current_game["home_team"]
        print(f"{team} scored")
        trigger_led(team)

    if current_game["away_score"] > previous_game["away_score"]:
        team = current_game["away_team"]
        print(f"{team} scored")
        trigger_led(team)

def get_live_game():
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard"

    data = requests.get(url, timeout=10).json()

    event = data["events"][0]
    competitors = event["competitions"][0]["competitors"]

    game = {}

    for team in competitors:
        if team["homeAway"] == "home":
            game["home_team"] = team["team"]["displayName"]
            game["home_score"] = int(team["score"])

        else:
            game["away_team"] = team["team"]["displayName"]
            game["away_score"] = int(team["score"])

    return game

previous_game = get_live_game()

print("Starting game:")
print(previous_game)

while True:
    time.sleep(10)

    current_game = get_live_game()

    check_score_change(previous_game, current_game)

    previous_game = current_game
