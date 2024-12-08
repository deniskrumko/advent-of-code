import sys
from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from itertools import combinations
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'
OOB, EMPTY = '@', '.'


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, value: int) -> 'Point':
        return Point(self.x * value, self.y * value)

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Puzzle:
    """Class for solving puzzle."""

    def __init__(self, data: str):
        """Initialize class instance."""
        self.data = [list(line) for line in data.splitlines()]
        self.antennas: dict[str, set[Point]] = defaultdict(set)
        self.antinodes: set[Point] = set()

        # Find all antennas on map and save them by groups
        for p in self.points:
            if (val := self.val(p)) != EMPTY:
                self.antennas[val].add(p)

    def find_antinodes(self, max_distance: int, self_count: bool) -> int:
        """Find all antinodes on map."""
        for grouped_antennas in self.antennas.values():
            for pair in combinations(grouped_antennas, 2):
                a, b = pair
                vector = a - b

                self.find_on_vector(a, vector, max_distance)
                self.find_on_vector(b, vector * -1, max_distance)

                if self_count:
                    self.antinodes.update((a, b))

        return len(self.antinodes)

    def find_on_vector(self, start: Point, vector: Point, max_distance: int):
        """Find all antinodes on vector in one direction."""
        for n in range(1, max_distance + 1):
            pos = start + vector * n
            if self.val(pos) == OOB:
                break

            self.antinodes.add(pos)

    # Helpers

    @property
    def points(self):
        """Get iterator over all points in puzzle."""
        for i in range(self.total_lines):
            for j in range(self.total_char_in_line):
                yield Point(i, j)

    def val(self, point: Point) -> str:
        """Get string value of point on puzzle."""
        if not (0 <= point.x < self.total_lines) or not (0 <= point.y < self.total_char_in_line):
            return OOB  # out of bounds

        return self.data[point.x][point.y]

    @cached_property
    def total_lines(self) -> int:
        return len(self.data)

    @cached_property
    def total_char_in_line(self) -> int:
        return len(self.data[0])


def function_1(data: str) -> int:
    """Get result for puzzle (part 1)."""
    return Puzzle(data).find_antinodes(max_distance=1, self_count=False)


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return Puzzle(data).find_antinodes(max_distance=sys.maxsize, self_count=True)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
