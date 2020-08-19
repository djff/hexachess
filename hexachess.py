import threading
import time

from aluLib import *
from player import *
from board import Board

window_width = 600
window_height = 600

grid = [[0, 0, 200, 200], [0, 200, 200, 400], [0, 400, 200, 600],
        [200, 0, 400, 200], [200, 200, 400, 400], [200, 400, 400, 600],
        [400, 0, 600, 200], [400, 200, 600, 400], [400, 400, 600, 600]]

board = Board(3, 3, grid)


def mainFrame():
    """
    This method is used to draw the board with each player's piece.
    It creates an object of the board class then uses the appropriate
    methods to draw the game board from the predefined grid.
    :return:
    """
    clear()
    board.draw_board()  # uses the draw_board method to create draw out a board
    game_state = board.get_state()
    for s_i in range(board.get_rows()):
        for p_i in range(board.get_columns()):
            if game_state[s_i][p_i] > 0:
                if game_state[s_i][p_i] == 2:
                    set_fill_color(1, 0, 1)  # Fill Color for player 2
                else:
                    set_fill_color(0, 1, 1)  # Fill Color for player 1
                draw_circle(player_state_pos[s_i][p_i][0], player_state_pos[s_i][p_i][1], 50)


def game_logic():
    """
    This method structures the algorithm for playing a game between players
    or against the computer. I runs in a separate thread from the graphics.

    LOGIC:
    First we ask the user if they want to play against a human or a computer,
    according to their response, we ask the user to input the start and stop
    coordinates, then we ask the players opponent to do the same. If the coordinates
    are valid, we perform the move and update the game state, the UI eventually updates
    as the game state changes.
    If the coordinates are not valid, then the user is asked to re-enter the coordinates.
    :return:
    """
    print("Hello, Welcome to Hexachess. ")

    choice = int(input("key in 1 to play against Human or 2 to play against AI: "))  # ask use to choose their opponent
    comp = False
    player = 1
    if choice == 1:
        player = randint(1, 2)  # Randomize which player is to start using the python random library

    game_num = 1
    # file to store Game as user plays the game.
    fp = open("game_played{}.txt".format(game_num), 'w')  # file used to store moves made in a game
    while True:
        game_state = board.get_state()
        print("::: Current game state :::")

        # display current game state as a grid
        for position in game_state:
            print(position)

        if choice == 1:  # if choice is one, means 2 players play against each other
            player = (player % 2) + 1  # Switch between players using the binary operator
            print("::: Player {} is to make a move :::".format(player))

            cur_pos, next_pos = get_coords(player, fp) # Get players coordinates.

        else:  # Player plays against Computer
            if not comp:
                print("::: Player {} is to make a move :::".format(player))
                cur_pos, next_pos = get_coords(player, fp)
                comp = True
            else:
                cur_pos, next_pos = get_coords("comp", fp)  # Get Computer's move
                time.sleep(0.7)  # Sleep to give a realistic effect to the game
                comp = False

        num = game_state[cur_pos[0]][cur_pos[1]]
        game_state[cur_pos[0]][cur_pos[1]] = 0

        game_state[next_pos[0]][next_pos[1]] = num

        if board.check_winning_state(player):
            print("###################################")
            print("#### Player {} has won the game ####".format(player))
            print("####################################")
            fp.write("###################################\n")
            fp.write("#### Player {} has won the game ####\n".format(player))
            fp.write("###################################\n")
            fp.close()
            cont = input("Game Over, type 'Y' to continue or anything to quit: ")  # Asks if player wants to continue
            if cont.lower() == 'y':
                game_num += 2
                fp = open("game_played{}.txt".format(game_num), 'w')
                board.set_state()  ##
                continue
            else:
                print("Thank you for playing. See ya next time!!!")
                break


def get_coords(player, fp):
    """
    This method gets a players or computer coordinates and check if it's valid.
    if yes, it returns the coordinates else it keeps asking until it gets a valid coord

    :param player: This is the current player making the move
    :param fp: This is the file where moves are written to
    :return: returns the current position coordinate and the next position coordinate
    """
    user = Player()
    while True:
        if player == "comp":
            cur_pos, next_pos = user.get_comp_coords(board.game_state)  # Get computer's coords
            player = 2
        else:
            cur_pos, next_pos = user.get_player_coords()  # Get Player's coords
        if not board.check_validity(cur_pos, next_pos, player, fp):  # Check if coords gotten makes a valid move
            print("::: [Error], Invalid entry for player {} :::".format(player))
            continue
        break

    return cur_pos, next_pos


threading.Thread(target=game_logic).start()  # Calls game_logic as a separate thread to avoid interrupting the graphics


# The following code calls the Start graphics function from the ALULib Library to initiate the graphical output of
# the defined program.
start_graphics(mainFrame, width=window_width, height=window_height, title='HexaChess', frames=5)
