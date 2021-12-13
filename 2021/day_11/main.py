from copy import deepcopy
from typing import Iterator


def get_adjacent_points(data: list, i: int, j: int) -> Iterator[tuple[int]]:
    """Get coordinates of adjacent points (including diagonals)."""
    max_x = len(data)
    max_y = len(data[0])

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == y == 0:
                continue

            x_coordinate = i + x
            if not (0 <= x_coordinate < max_x):
                continue

            y_coordinate = j + y
            if not (0 <= y_coordinate < max_y):
                continue

            yield x_coordinate, y_coordinate


def simulate_step(data: list) -> tuple:
    """Simulate single step in octopuses life 🐙."""
    data = deepcopy(data)
    initial_increment = True

    flashed_points, total_flashes = [], 0
    while True:
        for i in range(len(data)):
            for j in range(len(data[0])):
                if initial_increment:
                    data[i][j] += 1

                if data[i][j] > 9:
                    data[i][j] = 0
                    flashed_points.append((i, j))

        if not flashed_points:
            break  # reaction stopped

        total_flashes += len(flashed_points)
        for flashed_point in flashed_points:
            for ap in get_adjacent_points(data, *flashed_point):
                adjacent_point = data[ap[0]][ap[1]]
                if adjacent_point == 0:
                    continue

                data[ap[0]][ap[1]] += 1

        flashed_points = []
        initial_increment = False

    return data, total_flashes


def count_flashes_per_step(data: list, steps: int) -> int:
    """Count total amount of flashes during making all steps."""
    current_map = data
    total_flashes = 0
    for _ in range(steps):
        new_map, flashes = simulate_step(current_map)
        current_map = new_map
        total_flashes += flashes

    return total_flashes


def find_all_flashed_simultaneously(data: list) -> int:
    """Find step when all octopuses flashed simultaneously."""
    step, expected_flashes = 1, len(data) * len(data[0])
    current_map = data

    while True:
        new_map, total_flashes = simulate_step(current_map)
        if total_flashes == expected_flashes:
            return step

        current_map = new_map
        step += 1


if __name__ == '__main__':
    with open('2021/day_11/input.txt', 'r') as f:
        input_data = [[int(char) for char in line.strip()] for line in f.readlines()]
        print(f'Your result (1): {count_flashes_per_step(input_data, 100)}')
        print(f'Your result (2): {find_all_flashed_simultaneously(input_data)}')
