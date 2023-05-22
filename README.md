# "Rock Paper Scissors" Game


A student project inolving using Python to create a console based "Rock Paper Scissors" game


![Rock Paper Scissors game](/images/RPS.png)


**"Rock Paper Scissors"** is a two-player game, where both of the participants simultaneously pick one of three possible shapes/options - "rock", "paper" or "scissors". The game has three possible outcomes for the main player facing their computer opponent - win, draw or loss. Here are the conditions for a win:
* **Rock** beats **Scissors**
* **Scissors** beats **Paper**
* **Paper** beats **Rock**

If both players have chosen the same option, that leads to a draw.


## Implementing the game with Python

### Player move logic

At the start of the game the player is asked to choose an option, using the appropriate key for it (case insensitive):
* Rock - `R` or `r`
* Paper - `P` or `p`
* Scissors - `S` or `s`

If the player inputs anything other than those possible options, the program displays an error message and repeats the process until a correct input is entered.

### Computer move logic

After the player has chosen a move, the computer randomly picks a move (using the `randint()` method).

### Player vs Computer output and scoring

Depending on the moves of both parties, there are three possible outcomes, each connected with a scoring system as well:
* Player wins - the *player* gets **3 points** and the *computer* loses **1 point**
* Draw - both participants get **1 point**
* Computer wins - the *player* loses **1 point** and the *computer* wins **3 points**

### Restart or Quit options

The player is asked if they would like to **continue playing** or **end the game**, with two possible inputs - `Y` to continue playing the game or `N` to quit. If the player chooses the first option, the whole game process is looped to the beginning. If they choose to end the game, the program displays the final scores of both participants (if any of the players has a negative score, their score is displayed as 0) and the program exits.


![Demo console preview](/images/demo_screenshot.png)

## Important Links


**Link to the source code** - [Source code](rock_paper_scissors.py)

**Replit live demo** - https://replit.com/@WolfeRTs/rockpaperscissors#main.py
