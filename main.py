def trigger_led(team_colour):
    print(f"LED effect: {team_colour}")


previous_score = 98
current_score = 100

if current_score > previous_score:
    trigger_led("red")

