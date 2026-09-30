def display_title():
    print("===============================================================================")
    print("                            ROCK PAPER SCISSORS")
    print("===============================================================================")


def display_choices():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")


def display_result(result):

    if result == "draw":
        print("It's a draw!")

    elif result == "player":
        print("You win!")

    elif result == "computer":
        print("Computer wins!")


def display_score(player_score, computer_score):
    print("Player Score:", player_score)
    print("Computer Score:", computer_score)