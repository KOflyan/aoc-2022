import string
from typing import List

from utils import read_input

lower = {
    k: i + 1
    for i, k
    in enumerate(string.ascii_lowercase)
}

upper = {
    k: i + 27
    for i, k
    in enumerate(string.ascii_uppercase)
}


def solve(lines: List[str]):
    score = 0

    for i in range(0, len(lines), 3):
        # part 1
        ################################
        # c1, c2 = line[:len(line) // 2], line[len(line) // 2:]
        # common = set(c1).intersection(set(c2))
        ################################

        # part 2
        ################################
        group = lines[i:i + 3]

        common = set()
        for line in group:
            line = line.strip()
            if not common:
                common = set(line)
            else:
                common = common.intersection(set(line))
        ################################

        score += sum([
            lower[v] if v in lower else upper[v]
            for v
            in common
        ])

    print(score)


if __name__ == '__main__':
    data = read_input('input.txt')

    solve(data)
