from aluLib import *


class Board:
    """
    Board class is used to draw a board and validate
    any move made by the players, also determines
    if the board is in a winning state.
    """
    def __init__(self, rows, columns, grid):
        """
        Board Class constructure to create memory space
        and initialise object variables.
        :param rows: number of rows on the board
        :param columns: number of columns on the board
        :param grid: board representation in grid format
        """
        self.rows = rows
        self.columns = columns
        self.grid = grid
        self.game_state = []
        self.set_state()  # sets the initial game state

    def draw_board(self):
        """
        Method draws a board from it's grid representation
        setting even cells as black and odd cells as white
        :return: None
        """
        r = 1
        for row in self.grid:
            if (r % 2) == 1:
                set_fill_color(0, 0, 0)  # odd cells as white
            else:
                set_fill_color(1, 1, 1)  # even cells as black
            r += 1
            draw_rectangle(row[0], row[1], row[2], row[3])  # draw the rectangle using predefined coords

    def set_state(self):
        """
        sets the initial game state
        :return: None
        """
        self.game_state = [[2, 2, 2], [0, 0, 0], [1, 1, 1]]

    def get_state(self):
        """
        used to access the game state
        :return: current game_state
        """
        return self.game_state

    def get_rows(self):
        """
        used to get the number of rows on the board
        :return: number of rows
        """
        return self.rows

    def get_columns(self):
        """
        used to get the number of columns of the board
        :return: number of columns
        """
        return self.columns

    def out_of_grid(self, cur_coord, next_coord):
        """
        Checks if any of the coordinates are out of the grid
        :param cur_coord: current coordinate
        :param next_coord: next coordinate
        :return: True if it's out of the grid, False otherwise
        """
        return cur_coord[0] < 0 or cur_coord[1] > self.rows or next_coord[0] < 0 or next_coord[1] > self.columns

    def check_validity(self, cur_pos, next_pos, player, fp=None):
        """
        Performs a series of check to validate a move using its
        from and to coordinates
        :param cur_pos: from coordinate
        :param next_pos: to coordinate
        :param player: current player who made the move
        :param fp: file to write the move made in it
        :return: True if move is valid or False otherwise
        """
        cur_cell_val = self.game_state[cur_pos[0]][cur_pos[1]]  # get current cell player
        next_cell_val = self.game_state[next_pos[0]][next_pos[1]]  # get next cell player

        if next_cell_val == cur_cell_val:  # Player cannot capture it's piece, hence move should be invalid
            return False

        if cur_cell_val != player:  # if player is not using his piece, then validity should be False
            return False

        elif self.out_of_grid(cur_pos, next_pos):  # if any or both coords are out of grid, return not valid
            return False

        else:
            if player == 2:
                return self.valid_move_down(cur_pos, next_pos, fp)  # check if move is a valid move down for player 2
            else:
                return self.valid_move_up(cur_pos, next_pos, fp)  # check if move is a valid move up for player 1

    def valid_move_down(self, cur_pos, next_pos, fp):
        """
        Check if the move made by player 2 is a valid move down
        it can either be a vertical move down or a left/right capture down
        :param cur_pos: from coordinate
        :param next_pos: to coordinate
        :param fp: file to write the move performed
        :return: True if it's a valid move down or false otherwise
        """
        value = self.game_state[next_pos[0]][next_pos[1]]  # get value of the to cell
        player = self.game_state[cur_pos[0]][cur_pos[1]]   # get the current player

        # Check if it is a vertical move and if the landing cell is empty
        if cur_pos[0] == next_pos[0] - 1 and cur_pos[1] == next_pos[1] and value == 0:
            if fp:
                # Write move to file if it is valid
                fp.write("Player 2 moves down with from coordinates {} and to coordinates {}\n".
                         format(cur_pos, next_pos))
            return True

        # if the above fails, check if it's a capture. If yes, then the columns should be different. 2 scenarios here.
        # scenario1: Check if it's a right capture and if the value of the landing cell has the opponents piece
        # scenario2: check if it's a left capture and if the value of the landing cell has the opponents piece
        elif cur_pos[1] != next_pos[1]:
            if ((cur_pos[0] == next_pos[0] - 1 and cur_pos[1] == next_pos[1] - 1) or
                    (cur_pos[0] == next_pos[0] - 1 and cur_pos[1] == next_pos[1] + 1)) and value == (player % 2) + 1:
                if fp:
                    fp.write("Player 2 captures player 1 with from coordinates {} and to coordinates {}\n".
                             format(cur_pos, next_pos))
                return True
            else:
                return False  # return false if both both checks fail

    def valid_move_up(self, cur_pos, next_pos, fp):
        """
        Check if the move made by player 1 is a valid move up
        it can either be a vertical move up or a left/right capture up
        :param cur_pos: from coordinate
        :param next_pos: to coordinate
        :param fp: file to write the move performed
        :return: True if it's a valid move up or false otherwise
        """
        value = self.game_state[next_pos[0]][next_pos[1]]  # get value of to cell
        player = self.game_state[cur_pos[0]][cur_pos[1]]  # get value of from cell

        # Check if it is a vertical up and if the to cell is empty
        if cur_pos[0] == next_pos[0] + 1 and cur_pos[1] == next_pos[1] and value == 0:
            if fp:
                fp.write("Player 1 moves up with start coordinates {} and stop coordinates {}\n".
                         format(cur_pos, next_pos))
            return True

        # if the above fails, check if it's a capture. If yes, then the columns should be different. 2 scenarios here.
        # scenario1: Check if it's a right upward capture and if the value of the landing cell has the opponents piece
        # scenario2: check if it's a left upward capture and if the value of the landing cell has the opponents piece
        elif cur_pos[1] != next_pos[1]:
            if ((cur_pos[0] == next_pos[0] + 1 and cur_pos[1] == next_pos[1] - 1) or
                    (cur_pos[0] == next_pos[0] + 1 and cur_pos[1] == next_pos[0] + 1)) and value == (player % 2) + 1:
                if fp:
                    # write valid move to file
                    fp.write("Player 1 captures player 2 with from coordinates {} and to coordinates {}\n".
                             format(cur_pos, next_pos))
                return True
            else:
                return False

    def check_possible_move(self, player, row, column):
        """
        This is a helper method to check if any piece given
        to it has a valid move it can make.
        :param player: current player
        :param row: x-coordinate of starting cell
        :param column: y-coordinate of starting cell
        :return: True if there is a valid move found, false otherwise
        """

        # if it is player 1, the start row should begin from the upper row, which is current_row -1
        # if it's player 2, the start row should begin on the current row
        start_row = row - 1 if player == 1 else row

        # Same as above, player1's valid checks should stop on the current row and player2 on the next row (current + 1)
        stop_row = row if player == 1 else row + 1

        for i in range(start_row, stop_row + 1):
            for j in range(column - 1, column + 2):
                # rejects negative coords, out of grid coords and cells with same coordinates
                if 0 <= i < self.rows and 0 <= j < self.columns and not (i == row and j == column):
                    if self.check_validity([row, column], [i, j], player):
                        return True
        return False

    def check_winning_state(self, player):
        """
        Check if the board is in a winning state, if yes,
        the current player who made the last move is the winner
        :param player: Current player
        :return: True if board is in winning state, false otherwise
        """
        move_count = move_count_opp = 0  # count if current player or opponent has any valid move
        p1_count = p2_count = 0  # count the number of pieces of each player on the board
        opp = (player % 2) + 1  # get the player's opponent
        for i in range(self.rows):
            for j in range(self.columns):
                if self.game_state[i][j] == 2:
                    p2_count += 1  # increment if a piece for player 2 is found
                elif self.game_state[i][j] == 1:
                    p1_count += 1  # increment if a piece for player 1 is found

                # if any of the pieces are found on the opponent's end, then the game is won
                if (self.game_state[i][j] == 1 and i == 0) or (self.game_state[i][j] == 2 and i == 2):
                    return True
                if self.game_state[i][j] == player:
                    if self.check_possible_move(player, i, j):
                        move_count += 1  # increment if valid move has been found for current player
                elif self.game_state[i][j] == opp:
                    if self.check_possible_move(opp, i, j):
                        move_count_opp += 1  # increment if valid move has been found for opponent

        if not (p1_count and p2_count):  # if a player's pieces have all been captured, game is over
            return True

        return move_count < 1 and move_count_opp < 1  # if a player doesn't have any valid move, game is over

