from random import randint

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

# Player move logic
player_input = input("Choose [R]ock, [P]aper or [S]cissors: ")

if player_input.upper() == 'R':
    player_move = rock
elif player_input.upper() == 'P':
    player_move = paper
elif player_input.upper() == 'S':
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

# Computer move logic
computer_random_number = randint(1, 3)

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

# Player vs Computer logic and output
print(f"You chose: {player_move}")
print(f"Your opponent chose: {computer_move}")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")
