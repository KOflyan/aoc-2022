from typing import List, Callable, Any

from utils import read_input


def solve(lines: List[str]):
    cycles_to_consider = set(range(20, 221, 40))
    signal_strengths = []
    rendered_image = ''

    register_value = 1
    cycle_nr = 1
    sprite_index = [0, 1, 2]

    for line in lines:
        cmd = line.strip()

        cycles_required = 1 if cmd == 'noop' else 2

        for i in range(cycles_required):
            rendered_image += '#' if (cycle_nr - 1) % 40 in sprite_index else '.'

            if cycle_nr > 0 and cycle_nr % 40 == 0:
                rendered_image += '\n'

            cycle_nr += 1

            if i == 1 and cmd.startswith('addx'):
                register_value += int(cmd[cmd.rindex(' '):])

            sprite_index = [register_value - 1, register_value, register_value + 1]

            if cycle_nr in cycles_to_consider:
                signal_strengths.append(cycle_nr * register_value)

    print(f'Part 1: {sum(signal_strengths)}\n{"-":->15}\n')
    print(f'Part 2\n{"-":->15}')
    print(rendered_image)


if __name__ == '__main__':
    data = read_input('input.txt')
    solve(data)
