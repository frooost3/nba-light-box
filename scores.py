import json
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
    "home_score": 98,
    "away_team": "Boston Celtics",
    "away_score": 95
}

current_game = {
    "home_team": "Toronto Raptors",
    "home_score": 98,
    "away_team": "Boston Celtics",
    "away_score": 97
}

check_score_change(previous_game, current_game)

