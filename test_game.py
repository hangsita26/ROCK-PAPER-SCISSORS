from game_logic import determine_winner


def test_rock_vs_scissors():
    result = determine_winner("1", "Scissors")

    if result == "player":
        print("Test 1 passed: Rock beats Scissors")
    else:
        print("Test 1 failed")


def test_rock_vs_paper():
    result = determine_winner("1", "Paper")

    if result == "computer":
        print("Test 2 passed: Paper beats Rock")
    else:
        print("Test 2 failed")


def test_paper_vs_rock():
    result = determine_winner("2", "Rock")

    if result == "player":
        print("Test 3 passed: Paper beats Rock")
    else:
        print("Test 3 failed")


def test_scissors_vs_paper():
    result = determine_winner("3", "Paper")

    if result == "player":
        print("Test 4 passed: Scissors beats Paper")
    else:
        print("Test 4 failed")


def test_draw():
    result = determine_winner("1", "Rock")

    if result == "draw":
        print("Test 5 passed: Same choices result in a draw")
    else:
        print("Test 5 failed")


test_rock_vs_scissors()
test_rock_vs_paper()
test_paper_vs_rock()
test_scissors_vs_paper()
test_draw()