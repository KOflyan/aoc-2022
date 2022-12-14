from typing import List

import numpy as np

from utils import read_input

move_mapping = dict(
    R=np.array([1, 0]),
    L=np.array([-1, 0]),
    U=np.array([0, 1]),
    D=np.array([0, -1])
)


def solve(lines: List[str], knots: int):
    knot_positions = np.zeros((knots, 2))
    tail_visited = set()

    for line in lines:
        direction, moves = line.split()

        for _ in range(int(moves)):
            knot_positions[0] += move_mapping[direction]

            for i in range(1, len(knot_positions)):
                position_diff = knot_positions[i - 1] - knot_positions[i]

                if np.abs(position_diff).max() < 2:
                    continue

                knot_positions[i] += np.nan_to_num(position_diff // np.abs(position_diff))

            tail_visited.add(str(knot_positions[-1]))

    print(len(tail_visited))


if __name__ == '__main__':
    data = read_input('input.txt')
    solve(data, 2)  # p1
    solve(data, 10)  # p2
