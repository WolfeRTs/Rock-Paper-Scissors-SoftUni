from random import randint

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'


while True:

    # Player move logic
    player_input = input("Choose [R]ock, [P]aper or [S]cissors: ")

    if player_input.upper() == 'R':
        player_move = rock
    elif player_input.upper() == 'P':
        player_move = paper
    elif player_input.upper() == 'S':
        player_move = scissors
    else:
        print("\033[1;31Invalid Input. Try again...")
        continue

    # Computer move logic
    computer_random_number = randint(1, 3)

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    # Player vs Computer logic and output
    print(f"\033[0;36mYou chose: {player_move}")  # 36 is cyan
    print(f"\033[0;36mYour opponent chose: {computer_move}")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print("\033[1;32mYou win!")  # 32 is green
    elif player_move == computer_move:
        print("\033[1;33mDraw!")  # 33 is yellow
    else:
        print("\033[1;31mYou lose!")  # 31 is red

    # Restart or quit the game
    end_input = input("\033[0;0mWould you like to play more?\nType [Y] to play again or [N] to quit: ")
    if end_input.upper() == 'N':
        print("Thank you for playing!")
        exit()
