def update_score(result, player_score, computer_score):

    if result == "player":
        player_score = player_score + 1

    elif result == "computer":
        computer_score = computer_score + 1

    return player_score, computer_score