# Version 2 of 2048 #

Run the Gamemain.py file for execution of game.

Functionality of different files used is as follows:

Gamemain.py :- It starts the game on terminal by loading both the computer players and then they compete with each other. Time for move is set as 2 seconds.

Display.py :- It is used to control the visual properties of the game board on the terminal.

Grid.py :- Used to define the grid object and includes useful functions for the grid.

Helper.py :- Includes the eval function which is used to evaluate the heuristic score for a given configuration and other ulitily functions are defined.

Minimaxa.py :- The minimax algorithm along with alpha beta pruning is defined.

Max_Player.py :- The Max player functioning is defined that gets the next move for the player using Minimax Algorithm.

Min_Player.py :- The Min player functionality, here The getMove() function is present that returns a tuple (x, y) indicating the place you can place a tile.

