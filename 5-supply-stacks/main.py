import re
from typing import List

from utils import read_input_as_str


def parse_rearrangement_procedure_diagram(diagram: str) -> List[List[str]]:

    lines = diagram.split('\n')
    result = [
       [] for _ in range(int(lines[-1].split()[-1]))
    ]

    for line in lines[:-1]:
        for i in range(0, len(line), 4):
            crate = line[i:i + 4].strip()

            if len(crate) == 0:
                continue

            result[i // 4].insert(0, crate)

    return result


def solve(file_contents: str):
    diagram, instructions = file_contents.split('\n\n')
    instructions = instructions.strip().split('\n')

    parsed_diagram = parse_rearrangement_procedure_diagram(diagram)

    for instruction in instructions:
        move_n, move_from, move_to = map(int, re.sub(r'move|from|to', '', instruction).split())

        # part one
        ################################
        # parsed_diagram[move_to - 1].extend(parsed_diagram[move_from - 1][-move_n::][::-1])
        ################################

        # part 2
        ################################
        parsed_diagram[move_to - 1].extend(parsed_diagram[move_from - 1][-move_n::])
        ################################

        del parsed_diagram[move_from - 1][-move_n::]

    result = ''
    for row in parsed_diagram:
        result += re.sub(r'[]\[]', '', row[-1])

    print(result)


if __name__ == '__main__':
    data = read_input_as_str('input.txt')
    solve(data)
