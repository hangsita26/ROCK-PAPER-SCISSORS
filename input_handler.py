def get_player_choice():
    choice = input("Enter your choice:")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Please enter 1,2,or 3")

    return choice