import random
from game_config import CHOICES


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(choice, computer_choice):
    if choice == "1" and computer_choice == "Rock":
        return "draw"

    elif choice == "1" and computer_choice == "Scissors":
        return "player"

    elif choice == "1" and computer_choice == "Paper":
        return "computer"

    elif choice == "2" and computer_choice == "Paper":
        return "draw"

    elif choice == "2" and computer_choice == "Rock":
        return "player"

    elif choice == "2" and computer_choice == "Scissors":
        return "computer"

    elif choice == "3" and computer_choice == "Scissors":
        return "draw"

    elif choice == "3" and computer_choice == "Rock":
        return "computer"

    elif choice == "3" and computer_choice == "Paper":
        return "player"

    return "invalid"