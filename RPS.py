import random

def player(prev_play, opponent_history=[]):

    # Store opponent moves
    if prev_play != "":
        opponent_history.append(prev_play)

    # Counter moves
    ideal_response = {
        "P": "S",
        "R": "P",
        "S": "R"
    }

    # First move
    if len(opponent_history) < 3:
        return "R"

    # Predict next move based on last 3 plays
    last_three = "".join(opponent_history[-3:])

    patterns = {}

    for i in range(len(opponent_history) - 3):
        pattern = "".join(opponent_history[i:i+3])
        next_move = opponent_history[i+3]

        if pattern == last_three:
            if next_move in patterns:
                patterns[next_move] += 1
            else:
                patterns[next_move] = 1

    if patterns:
        prediction = max(patterns, key=patterns.get)
        return ideal_response[prediction]

    # Fallback random move
    return random.choice(["R", "P", "S"])
