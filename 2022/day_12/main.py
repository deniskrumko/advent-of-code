from pathlib import Path

import numpy as np

INPUT_FILE = Path(__file__).parent / 'input.txt'
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def walk(cur, m, paths, walked):
    if tuple(cur) in walked:
        return  # already was

    cur_val = m[tuple(cur)]
    if cur_val == 'E':
        paths.append(len(walked))
        return

    walked += (tuple(cur), )

    for d in DIRECTIONS:
        new_cur = cur + d
        if 0 <= new_cur[0] < len(m) and 0 <= new_cur[1] < len(m[0]):
            new_cur_val = m[tuple(new_cur)]
            if cur_val == 'S':
                cur_val = 'a'
            if new_cur_val == 'E':
                new_cur_val = 'z'

            if abs(ord(cur_val) - ord(new_cur_val)) <= 1:
                walk(new_cur, m, paths, walked)
            else:
                # too high step
                continue
        else:
            # out of map
            continue


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    m = np.array([
        np.array([char for char in line])
        for line in data.splitlines()
    ])
    start = np.array([i[0] for i in np.where(m == 'S')])
    # end = np.array([i[0] for i in np.where(m == 'E')])

    paths = []

    walk(start, m, paths, tuple())
    assert paths
    return min(paths)


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return True


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
