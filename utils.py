from typing import List


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return f.readlines()


def read_input_as_str(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()
