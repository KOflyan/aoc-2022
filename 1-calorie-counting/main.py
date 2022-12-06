
def solve():
    with open('./input.txt', 'r') as f:

        result = sorted(
            map(
                lambda row: sum([
                    int(e)
                    for e
                    in row.split('\n')
                ]),
                f
                .read()
                .strip()
                .split('\n\n')
            )
        )

    # part 1
    # print(sum(result))
    print(sum(result[-3:]))


if __name__ == '__main__':
    solve()
