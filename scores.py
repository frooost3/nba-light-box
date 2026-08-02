scores = [98, 98, 100, 103]

previous_score = scores[0]

for current_score in scores[1:]:
    if current_score > previous_score:
        print(f"Score increased from {previous_score} to {current_score}")
        print("Trigger LED effect")
    else:
        print("No score change")

    previous_score = current_score


