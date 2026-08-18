import json
import requests
import time
import board
import adafruit_pixelbuf 
from adafruit_raspberry_pi5_neopixel_write import neopixel_write

TEAM_COLOURS = {
    "Atlanta Dream": (200, 16, 46),
    "Chicago Sky": (65, 143, 222),
    "Connecticut Sun": (220, 68, 5),
    "Dallas Wings": (0, 83, 155),
    "Golden State Valkyries": (112, 71, 148),
    "Indiana Fever": (0, 45, 98),
    "Las Vegas Aces": (186, 12, 47),
    "Los Angeles Sparks": (85, 37, 130),
    "Minnesota Lynx": (0, 80, 131),
    "New York Liberty": (0, 171, 142),
    "Phoenix Mercury": (32, 24, 71),
    "Portland Fire": (206, 17, 38),
    "Seattle Storm": (45, 177, 53),
    "Toronto Tempo": (0, 120, 212),
    "Washington Mystics": (0, 43, 92),
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

    for _ in range(3):
        pixels.fill(colour)
        time.sleep(0.4)

        pixels.fill((0, 0, 0))
        time.sleep(0.25)

def check_score_change(previous_game, current_game):
    if previous_game["game_id"] != current_game["game_id"]:
        print("New game detected.")
        return

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

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        print(f"Network error: {error}")
        return None

    event = None 

    for game_event in data["events"]:
        status = game_event["status"]["type"]["state"]

        if status == "in":
            event = game_event
            break

    if event is None:
        print("No live WNBA game right now.")
        return None

    competitors = event["competitions"][0]["competitors"]

    game = {
        "game_id": event["id"]
    }

    for team in competitors:
        if team["homeAway"] == "home":
            game["home_team"] = team["team"]["displayName"]
            game["home_score"] = int(team["score"])

        else:
            game["away_team"] = team["team"]["displayName"]
            game["away_score"] = int(team["score"])

    return game

previous_game = None

while True:
    current_game = get_live_game()

    if current_game is None:
        time.sleep(30)
        continue

    if previous_game is not None:
        check_score_change(previous_game, current_game)

    previous_game = current_game
    time.sleep(10)
