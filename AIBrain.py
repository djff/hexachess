class AIBrain:
    """
        This is used to create the Brain of the Computer
        so at anytime it can know the state of the game
        and perform a move according to that state.
    """
    def __init__(self, states):
        """
        AIBrain constructor to create memory space and initialise
        object variables.

        :param states: text files holding possible board states
        """
        self.states = open(states, 'r')
        self.brain = {}

    def set_knowledge(self):
        """
        We create a dictionary object holding a board state and all it's
        possible movements (in coordinate form) from that state.
        :return:
        """
        num_of_states = int(self.states.readline())  # get the number of states in the the file
        for i in range(num_of_states):
            counter = 0
            moves = []  # stores a move containing start ands stop coords
            state = ''  # stores a particular board state associated to the moves.

            input_lines = int(self.states.readline())
            for j in range(input_lines):
                if input_lines-counter > 3:
                    moves.append([int(x) for x in self.states.readline().strip("\n").split(" ")])
                else:
                    # Represent a state as a string for easy referencing
                    state += "".join((self.states.readline().strip("\n").split(" ")))
                counter += 1
            self.brain[str(state)] = moves  # Create the computer's brain

    def get_brain(self):
        """
        Gives the computer's brain upon request
        :return: computer's brain (self.brain)
        """
        return self.brain
