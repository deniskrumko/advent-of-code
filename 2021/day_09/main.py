import math
from collections import Counter
from copy import deepcopy
from itertools import permutations
from string import ascii_lowercase
from typing import Iterator


def get_char_generator(size: int) -> Iterator[str]:
    """Create generator for characters.

    For example, output will be like 'aa', 'ab' and so on.
    """
    for c in permutations(ascii_lowercase, size):
        yield ''.join(c)


CHAR_SIZE = 2  # it's enough for puzzle input
CHAR_GENERATOR = get_char_generator(size=CHAR_SIZE)
BORDER = 'X' * CHAR_SIZE


def get_adjacent_points(data: list, i: int, j: int) -> Iterator[tuple[int]]:
    """Get coordinates of adjacent points."""
    max_x = len(data)
    max_y = len(data[0])

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == y == 0 or abs(x) == abs(y) == 1:
                continue

            x_coordinate = i + x
            if not (0 <= x_coordinate < max_x):
                continue

            y_coordinate = j + y
            if not (0 <= y_coordinate < max_y):
                continue

            yield x_coordinate, y_coordinate


def find_lowest_points(data: list) -> Iterator[int]:
    """Find all lowest points on map."""
    for i in range(len(data)):
        for j in range(len(data[0])):
            point = int(data[i][j])
            adjacent_points = (int(data[a[0]][a[1]]) for a in get_adjacent_points(data, i, j))
            if all(point < adjacent_point for adjacent_point in adjacent_points):
                yield point


def get_sum_of_lowest_points(data: list) -> int:
    """Get sum of values of lowest points on map."""
    lowest_points = list(find_lowest_points(data))
    return sum(lowest_points) + len(lowest_points)


def mark_basin_point(
    basins_map: list,
    i: int,
    j: int,
    basin_char: str = None,
):
    """Mark basin point with X or unique pair of characters."""
    point = basins_map[i][j]
    if not point.isdigit():  # already marked
        return

    point = int(point)
    if point == 9:  # it's a border
        basins_map[i][j] = BORDER
        return

    # mark current point using existing char or generate new unique char
    basin_char = basin_char or next(CHAR_GENERATOR)
    basins_map[i][j] = basin_char

    # Find all adjacent points and mark them with same basic char
    for a in get_adjacent_points(basins_map, i, j):
        adjacent_point_value = basins_map[a[0]][a[1]]
        if adjacent_point_value.isdigit():
            adjacent_point_value = int(adjacent_point_value)
            mark_basin_point(basins_map, *a, basin_char=basin_char)


def find_basins(data: list) -> int:
    """Find all basins on map and count product of three largest basins."""
    basins_map = deepcopy(data)  # because it will be overwritten
    max_i, max_j = len(basins_map), len(basins_map[0])

    # Walk the map and mark it
    for i in range(max_i):
        for j in range(max_j):
            mark_basin_point(basins_map, i, j)

    # Find all basins and get their sizes
    basins = Counter(sum(basins_map, []))
    assert sum(basins.values()) == max_i * max_j

    # Get product of three largest basins
    sorted_basins = sorted(basins, key=lambda x: basins[x], reverse=True)
    sorted_basins.remove(BORDER)  # borders not included
    return math.prod(basins[x] for x in sorted_basins[:3])


if __name__ == '__main__':
    with open('2021/day_09/input.txt', 'r') as f:
        input_data = [[j for j in i.strip()] for i in f.readlines()]
        print(f'Your result (1): {get_sum_of_lowest_points(input_data)}')
        print(f'Your result (2): {find_basins(input_data)}')
