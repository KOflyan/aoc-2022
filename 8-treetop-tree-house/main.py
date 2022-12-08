from typing import List

import numpy as np

from utils import read_input


def solve_1(tree_matrix: np.array):
    visible_trees = (sum(tree_matrix.shape) - 2) * 2

    for y in range(1, tree_matrix.shape[1] - 1):
        for x in range(1, tree_matrix.shape[0] - 1):
            tree_height = tree_matrix[y, x]

            is_visible = tree_height > get_min_tree_height_from_surrounding_trees(x, y, tree_matrix)

            visible_trees += int(is_visible)

    print(visible_trees)


def solve_2(tree_matrix: np.array):
    max_score = -1

    for y in range(1, tree_matrix.shape[1] - 1):
        for x in range(1, tree_matrix.shape[0] - 1):
            current_tree = tree_matrix[y, x]
            paths = [
                np.flip(tree_matrix[:y, x]),
                tree_matrix[y + 1:, x],
                np.flip(tree_matrix[y, :x]),
                tree_matrix[y, x + 1:]
            ]

            score = calculate_scenic_score(paths, current_tree)

            if score > max_score:
                max_score = score

    print(max_score)


def get_min_tree_height_from_surrounding_trees(
        x: int,
        y: int,
        tree_matrix: np.array
) -> int:
    return min(
        tree_matrix[:y, x].max(),
        tree_matrix[y + 1:, x].max(),
        tree_matrix[y, :x].max(),
        tree_matrix[y, x + 1:].max()
    )


def calculate_scenic_score(
    paths: List[np.array],
    current_tree: int
) -> int:
    score = 1
    for path in paths:
        trees_visible = 0

        for tree in np.nditer(path.flatten()):
            trees_visible += 1

            if tree >= current_tree:
                break

        score *= trees_visible
    return score


if __name__ == '__main__':
    data = read_input('input.txt')

    matrix = np.matrix([[*line.strip()] for line in data]).astype(int)

    solve_1(matrix)  # part 1
    solve_2(matrix)  # part 2

