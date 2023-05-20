from random import randint

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
score_player = 0
score_computer = 0


while True:

    # Player move logic
    player_input = input("\033[0;0mChoose [R]ock, [P]aper or [S]cissors: ")

    if player_input.upper() == 'R':
        player_move = rock
    elif player_input.upper() == 'P':
        player_move = paper
    elif player_input.upper() == 'S':
        player_move = scissors
    else:
        print("\033[1;31mInvalid Input. Try again...")
        continue

    # Computer move logic
    computer_random_number = randint(1, 3)

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    # Player vs Computer logic and output plus score logic
    print(f"\033[0;36mYou chose: {player_move}")  # 36 is cyan
    print(f"\033[0;36mYour opponent chose: {computer_move}")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print("\033[1;32mYou win!")  # 32 is green
        score_player += 3
        score_computer -= 1
    elif player_move == computer_move:
        print("\033[1;33mDraw!")  # 33 is yellow
        score_player += 1
        score_computer += 1
    else:
        print("\033[1;31mYou lose!")  # 31 is red
        score_player -= 1
        score_computer += 3

    # Restart or quit the game (print final result if quit)
    while True:
        end_input = input("\033[0;0mWould you like to play more?\nType [Y] to play again or [N] to quit: ")
        if end_input.upper() == 'N':
            if score_player < 0:
                score_player = 0
            if score_computer < 0:
                score_computer = 0
            print(f"Final score is:")
            print(f"\033[1;34mPlayer - {score_player} points")  # 34 is blue
            print(f"Computer - {score_computer} points")
            print("\033[0;0mThank you for playing!")
            exit()
        elif end_input.upper() == 'Y':
            break
        else:
            print("\033[1;31mInvalid Input!")
            continue
