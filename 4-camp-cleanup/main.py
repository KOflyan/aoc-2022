import itertools
from typing import List

from utils import read_input


def is_subset(s1: int, e1: int, s2: int, e2: int) -> bool:
    return (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1)


def is_overlap(s1: int, e1: int, s2: int, e2: int) -> bool:
    return is_subset(s1, e1, s2, e2) or (s1 <= s2 <= e1) or (s1 <= e2 <= e1)


def solve(lines: List[str]):
    score = 0

    for row in lines:

        range1, range2 = row.split(',')

        start1, end1 = list(map(int, range1.split('-')))
        start2, end2 = list(map(int, range2.split('-')))

        # part 1
        ################################
        # score += int(is_subset(start1, end1, start2, end2))
        ################################

        # part 2
        ################################
        score += int(is_overlap(start1, end1, start2, end2))
        ################################

    print(score)


if __name__ == '__main__':
    data = read_input('input.txt')

    solve(data)
