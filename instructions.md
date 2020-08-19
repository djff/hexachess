# Overview of the project


The inspiration for this project is heavily inspired by the following video. Watch it, then re-watch it, and make sure you get the ideas behind it before moving on to the rest of the instructions: [hexachess video](https://www.youtube.com/watch?v=sw7UAZNgGg8)

No clever AI work here however, you will have to build up 3 milestones as follows:

## Milestone 1: Visuals and basic data structures.

For this first milestone, we will have to brush up on our ALULib skills. As a first step, draw the board, with all the pieces on it. You may want to take a look at the various ALULib functions [here](http://projectpython.net/chapter19/)

Your first step should be to just draw a simple grid, then 6 circles representing the pieces of each player. 

In doing so, take note of the coordinates you use to draw these circles. If I am player 1 and want to move a piece forward, where does that mean the circle should be drawn? how do the coordinates change?

As a second step, make sure to store information about each circle in some kind of 2d list, so that we can keep track of their position over time. Your code right now should go through the 2d list, and draw a circle in the right place in the screen based on what the 2d list represents. For example board = [[2, 2, 2], [0, 0, 0], [1, 1, 1]] would describe the initial state of the game, while board = [[2,0,2], [2, 0, 1], [0, 1, 0]] would represent a very different position, something like: 
`
2  _  2
2  _  1
_  1  _
`

At this point you should be able to modify the board 2d list, and that will result in the state of the game being drawn completely differently!

## Milestone 2: Gameplay
Time for some interaction! Your first step should be to create a function that asks the user to identify a piece (using the coordinates), then the coordinates of where the user wants to move the piece. The screen should then change to reflect the new board state - make sure to use the 2d list from Milestone 1.

This function should be called repeatedly in your drawing loop.

As it is however, it would be very easy for anyone to cheat, so for the next step, we should make sure to enforce some rules:
- First, time to keep track of the players using some global variable that gets incremented each round. The valid moves for player 1 are different from the valid moves for player 2. Make sure that the function above now prints which player is supposed to play.
- Secondly, check the initial coordinates for the piece the player wants to move, here we need to insure that the coordinates are on the board AND that there is a piece in that spot AND that the piece belongs to the right player.
- Finally, make sure that the target destination is correct: It should be on the board AND one of two options: Either move forward a step if that spot is empty, or move forward and diagonally if an opposing piece is there.

In all these scenarios, the board should correctly reflect the new move. This will bring you to the end of milestone 2.

## Milestone 3: Saving, random start, basic AI, win condition.

You have 2 weeks for this set of tasks, and they will take you to a few different directions. All the previous milestones are pre-requisite to this, but these tasks are more flexible, and do not have to be tackeld in order. Make sure to also study the grade allocation and prioritize your time and effort accordingly.

Task 1: Detecting that the game is won.
- So far, we do nothing to determine wether or not a player has won the game, you should build that up in your solution. Recall that the game can be one in one of 3 ways:
	- The current player can't make a valid move.
	- The current player has no pieces.
	- The current player just moved one of its pieces all the way to the apposite row. 

If the game is over, then you should offer the player the option to either start a new game, or exit the game (recall cs1_quit() lets you exit out)

Task 2: Saving a replay of the game.
Whenever someone exits the game, we should save a file which describes how the game went. This means that each line should describe what _move_ was played, until the game finishes. 

If you've done Task 1, then you should create and save a file whenever the game is done, regardless of whether or not the player wants to quit or restart.

If you choose not to do Task 1, then you should always give the player an option to quit when you ask them for input, and you should save when they do tell you they want to quit.

Task 3: Basic AI.
Upon starting the game, ask the user if they want to play against an AI. If they do, the AI must play simple random moves: The AI should know where each of its pieces are, what valid moves exist, and then play one of those valid moves.

Grading scheme:
Code quality - comments, functions, good logic: 10%

Milestone 1:
- Drawing the board: 2.5%
- Using a data structure for the state of the board: 2.5%

Milestone 2:
- Taking user input to determine pieces to move: 5%
- Correctly checking valid moves: 5%

Milestone 3:
- Auto detecting wins: 25%
- Saving the result of the game: 25%
- Basic AI player: 25%

Best of luck!
