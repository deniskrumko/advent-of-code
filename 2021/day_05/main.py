from collections import (
    Counter,
    defaultdict,
)


def build_map(data: list, use_diagonals: bool) -> defaultdict:
    """Build map using input data."""
    vents_map = defaultdict(int)
    for line in data:
        start, end = line.split(' -> ')
        start_x, start_y = [int(i) for i in start.split(',')]
        end_x, end_y = [int(i) for i in end.split(',')]

        is_straight = bool(start_x == end_x or start_y == end_y)
        if not use_diagonals and not is_straight:
            continue

        step_x = -1 if start_x > end_x else 1
        step_y = -1 if start_y > end_y else 1

        if is_straight:
            for i in range(start_x, end_x + step_x, step_x):
                for j in range(start_y, end_y + step_y, step_y):
                    vents_map[(i, j)] += 1
        else:
            j = start_y
            for i in range(start_x, end_x + step_x, step_x):
                vents_map[(i, j)] += 1
                j += step_y

    return vents_map


def find_intersections_on_map(data: list, use_diagonals: bool = False) -> int:
    """Count all intersections."""
    vents_map = build_map(data, use_diagonals)
    return sum(value for key, value in Counter(vents_map.values()).items() if key != 1)


if __name__ == '__main__':
    with open('2021/day_05/input.txt', 'r') as f:
        input_data = [i.strip() for i in f.readlines()]
        print(f'Your result (1): {find_intersections_on_map(input_data, False)}')
        print(f'Your result (2): {find_intersections_on_map(input_data, True)}')
