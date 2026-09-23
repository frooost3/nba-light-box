# NBA Light Box

A Raspberry Pi 5 project that monitors basketball scores and triggers team-coloured LED effects when a team scores.

The project combines Python, live sports data, GPIO control, and addressable LEDs to connect real-time software data with a physical hardware output.

## Demo

[![NBA Light Box Demo](https://img.youtube.com/vi/R0Dvx5Dux3g/maxresdefault.jpg)](https://youtube.com/shorts/R0Dvx5Dux3g)

*Click the image to watch the demo.*

The video uses simulated score input because no live game was available during recording. The score-detection, team identification, colour selection, Raspberry Pi control, and LED response are handled by the same functions used by the live program.

## How It Works

The program:

1. Retrieves live basketball scoreboard data.
2. Finds the game containing the selected team.
3. Stores the current scores for both teams.
4. Periodically retrieves the latest scores.
5. Compares the new scores with the previous scores.
6. Identifies which team scored.
7. Looks up that team's RGB colour.
8. Sends the appropriate signal from the Raspberry Pi to the LED strip.
9. Flashes the strip in the scoring team's colour.

For example:

Toronto Raptors score → LEDs flash red  
Boston Celtics score → LEDs flash green

## Hardware

- Raspberry Pi 5
- WS2812B addressable RGB LED strip
- SN74AHCT125N logic level shifter
- 5V external power supply
- 470Ω resistor
- 1000µF capacitor
- Breadboard and jumper wires

The Raspberry Pi controls the LED data signal through GPIO18. The SN74AHCT125N converts the Raspberry Pi's 3.3V logic signal to a 5V signal suitable for the LED strip.

## Software

- Python
- Requests
- Adafruit PixelBuf
- Raspberry Pi GPIO / NeoPixel control
- JSON scoreboard data

## Project Structure

`scores.py` — Retrieves score data, detects score changes, and controls the LEDs.

`demo.py` — Simulates score changes for demonstrating the hardware when no live game is available.

## Current Features

- Live basketball score monitoring
- Target-team game filtering
- Home and away score-change detection
- Team-specific RGB colours
- Physical LED response to scoring
- Network error handling
- Raspberry Pi 5 compatible NeoPixel control
- Demo mode for testing without a live game

## Future Improvements

- Add more NBA team colours
- Build a finished enclosure and LED diffuser
- Add a display for the current score
- Add automatic startup when the Raspberry Pi boots
- Improve logging and game-status information
- Connect with a speaker to play custom sounds when teams score

## Purpose

I built this project to gain experience combining software and hardware in a complete system. It gave me hands-on experience working with Python, APIs and JSON data, Raspberry Pi GPIO, digital electronics, debugging, and Git/GitHub.

