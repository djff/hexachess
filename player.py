from AIBrain import AIBrain
from random import randint
player_state_pos = [[[100, 100], [300, 100], [500, 100]],
                    [[100, 300], [300, 300], [500, 300]],
                    [[100, 500], [300, 500], [500, 500]]]


class Player:
    """
    This Class defines a human player and a computer player.
    we get the valid coordinates through this class since that's
    all a player can do.
    """
    def __init__(self):
        pass

    @staticmethod
    def get_player_coords():
        """
        Method gets a human player's coords and
        return to calling function
        :return:
        """
        cur_pos = input("Enter Row and Column separated by a space. Which piece do you want to move: ").split(" ")
        next_pos = input("Enter Row and Column separated by a space. Where do you want the piece to move: ").split(
            " ")
        cur_pos = [int(cur_pos[0]) - 1, int(cur_pos[1]) - 1]
        next_pos = [int(next_pos[0]) - 1, int(next_pos[1]) - 1]

        return cur_pos, next_pos

    def get_comp_coords(self, game_state):
        """
        This method gets the computer coordinates from the brain.
        it starts by checking if the current board state is in the brain,
        if not it creates a symmetrical representation of the current game state
        and gets all the possible moves from the brain, then randomly picks
        one of the moves to play.
        :param game_state: Current board game state
        :return: current possition coords and next position coords respectively
        """
        ai = AIBrain("states.txt")  # Creates an object of the AI's Brain
        ai.set_knowledge()  # load the knowledge into the brain
        ai_brain = ai.get_brain()

        # builds a string representation of the game state for lookup
        b_state = self.build_game_state_string(game_state)
        try:
            coords = ai_brain[b_state]  # Tries to get possible moves using the current board state
            coord = coords[randint(0, len(coords) - 1)]
        except KeyError:
            # if the above fails, get moves using the symmetrical representation of the board state
            coords = ai_brain[self.get_symmetry(game_state)]
            coord = coords[randint(0, len(coords) - 1)]

            # maintain symmetry on the move
            if coord[1] < 1:
                coord[1] += 2
            elif coord[1] > 1:
                coord[1] -= 2

            if coord[3] < 1:
                coord[3] += 2
            elif coord[3] > 1:
                coord[3] -= 2

        return [coord[0], coord[1]], [coord[2], coord[3]]  # return current and next position coords

    @staticmethod
    def build_game_state_string(state):
        """
        Builds a string representation of the board's state
        :param state: board state
        :return: b_state, string representation of the board state
        """
        b_state = ''
        for row in state:
            b_state += "".join([str(i) for i in row])
        return b_state

    def get_symmetry(self, game_state):
        """
        Get symmetrical representation of board state using the current board sate
        :param game_state: current board state
        :return: string representation of the symmetrical representation of current state
        """
        state = []
        for row in game_state:
            state.append([row[2], row[1], row[0]])  # Switch first column and last column
        return self.build_game_state_string(state)
