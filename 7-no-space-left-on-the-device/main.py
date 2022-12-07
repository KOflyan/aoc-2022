from dataclasses import dataclass, field
from typing import List, Dict

from utils import read_input


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    sub_dirs: list = field(default_factory=list)
    files: List[File] = field(default_factory=list)

    def shallow_size(self) -> int:
        return sum([f.size for f in self.files])

    def size(self) -> int:
        return self.shallow_size() + sum([d.size() for d in self.sub_dirs])


def compose_current_path(current_path: str, directory_name: str) -> str:
    if directory_name == '..':
        return current_path[:current_path[:-1].rindex('/') + 1]

    return f'{current_path}{directory_name.strip("/")}/'


def compose_filesystem_tree(lines: List[str]) -> Dict[str, Directory]:
    root = Directory('/')
    directory_by_path: Dict[str, Directory] = {
        root.name: root
    }

    current_path = ''

    for line in lines:

        if line.startswith('$ ls'):
            continue

        if line.startswith('$ cd'):
            directory_name = line.split('$ cd')[1].strip()

            current_path = compose_current_path(current_path, directory_name)

            directory_by_path[current_path] = directory_by_path.get(
                current_path,
                Directory(directory_name)
            )

        elif line.startswith('dir'):
            directory_name = line.split('dir')[1].strip()
            dir_path = f"{current_path}{directory_name}/"
            directory = Directory(directory_name)

            directory_by_path[current_path].sub_dirs.append(directory)
            directory_by_path[dir_path] = directory_by_path.get(
                dir_path,
                directory
            )

        elif not line.startswith('$'):
            size, name = line.split()

            directory_by_path[current_path].files.append(
                File(name, int(size))
            )

    return directory_by_path


def solve(lines: List[str]):

    tree = compose_filesystem_tree(lines)
    sorted_sizes = sorted([d.size() for d in tree.values()])

    # part 1
    #######################################################
    print(
        sum([v if v <= 100_000 else 0 for v in sorted_sizes])
    )
    #######################################################

    # part 2
    #######################################################
    to_free = 30_000_000 - (70_000_000 - sorted_sizes[-1])

    for v in sorted_sizes:
        if v >= to_free:
            print(v)
            break
    #######################################################


if __name__ == '__main__':
    data = read_input('input.txt')

    solve(data)
