from input_handler import get_player_choice
from game_logic import get_computer_choice, determine_winner
from score_manager import update_score
from display import display_title, display_choices, display_result, display_score


player_score = 0
computer_score = 0

display_title()
display_choices()

choice = get_player_choice()

computer_choice = get_computer_choice()

print("You chose:", choice)
print("computer chose:", computer_choice)

result = determine_winner(choice, computer_choice)

display_result(result)

player_score, computer_score = update_score(result, player_score, computer_score)

display_score(player_score, computer_score)