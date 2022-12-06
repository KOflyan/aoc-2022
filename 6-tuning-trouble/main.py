from utils import read_input_as_str


def solve(file_content: str) -> int:

    # part 1
    ##################################################
    # marker_len = 4
    ##################################################

    # part 2
    ##################################################
    marker_len = 14
    ##################################################

    for i in range(0, len(data) - marker_len):
        s = set(file_content[i:i + marker_len])

        if len(s) == marker_len:
            return i + marker_len


if __name__ == '__main__':
    data = read_input_as_str('input.txt')

    print(
        solve(data.strip())
    )