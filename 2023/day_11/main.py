from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


@dataclass
class Point:
    x: int
    y: int


def is_empty_vertical(data, y) -> bool:
    """Check if vertical line is empty."""
    return set(line[y] for line in data) == {'.'}


def is_empty_horizontal(data, x) -> bool:
    """Check if horizontal line is empty."""
    return set(data[x]) == {'.'}


def get_galaxies(data: str, expansion_size: int = 2) -> list[Point]:
    """Get list of galaxies from data."""
    data = [[v for v in line] for line in data.splitlines()]
    galaxies = []

    @lru_cache(maxsize=None)
    def is_empty_vertical_cached(y) -> bool:
        return is_empty_vertical(data, y)

    x_shift = 0
    for x in range(len(data)):
        if is_empty_horizontal(data, x):
            x_shift += (expansion_size - 1)
            continue

        y_shift = 0
        for y in range(len(data[0])):
            if is_empty_vertical_cached(y):
                y_shift += (expansion_size - 1)
                continue

            if data[x][y] == '#':
                galaxies.append(Point(x + x_shift, y + y_shift))
    return galaxies


def get_distance(galaxy_a: Point, galaxy_b: Point) -> int:
    """Get distance between two galaxies on square map."""
    return abs(galaxy_a.x - galaxy_b.x) + abs(galaxy_a.y - galaxy_b.y)


def function_1(data: str, expansion_size: int = 2) -> bool:
    """Get result for puzzle (part 1)."""
    galaxies = get_galaxies(data, expansion_size)
    return sum(
        get_distance(galaxy_a, galaxy_b)
        for galaxy_a, galaxy_b in combinations(galaxies, 2)
    )


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return function_1(data, expansion_size=1_000_000)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
