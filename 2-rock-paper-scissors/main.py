from os import path
from typing import List

import numpy as np

from utils import read_input

my_moves = 'XYZ'
opponents_moves = 'ABC'

# (rock, paper, scissors) x (rock, paper, scissors)
outcome_matrix = np.matrix([
    [3, 0, 6],
    [6, 3, 0],
    [0, 6, 3]
])


def solve(lines: List[str]):
    score = 0

    for line in lines:
        # part 1
        ################################
        # opponent_move, my_move = line.split()
        # opponent_move, my_move = opponents_moves.index(opponent_move), \
        #                          my_moves.index(my_move)
        # score += outcome_matrix.tolist()[my_move][opponent_move] + my_move + 1
        ################################

        # part 2
        ################################
        opponent_move, outcome = line.split()
        opponent_move, outcome = \
            opponents_moves.index(opponent_move), \
            my_moves.index(outcome) * 3

        my_move = outcome_matrix.transpose().tolist()[opponent_move].index(outcome)

        score += my_move + 1 + outcome
        ################################

    print(score)


if __name__ == '__main__':
    data = read_input('input.txt')

    solve(data)
