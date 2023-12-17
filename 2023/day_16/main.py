from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

INPUT_FILE = Path(__file__).parent / 'input.txt'


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Beam:
    point: Point
    direction: Point

    @property
    def next_point(self) -> Point:
        return self.point + self.direction

    def __hash__(self):
        return hash((self.point, self.direction))


UP, RIGHT, DOWN, LEFT = Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)
MIRRORS_MAP = {
    '\\': {RIGHT: DOWN, DOWN: RIGHT, LEFT: UP, UP: LEFT},
    '/': {RIGHT: UP, DOWN: LEFT, LEFT: DOWN, UP: RIGHT},
}
SPLITTERS_MAP = {
    '|': {RIGHT: [UP, DOWN], DOWN: [DOWN], LEFT: [UP, DOWN], UP: [UP]},
    '-': {RIGHT: [RIGHT], DOWN: [LEFT, RIGHT], LEFT: [LEFT], UP: [LEFT, RIGHT]},
}


class Maze:

    def __init__(self, data: str):
        self._data = [[ch for ch in line] for line in data.splitlines()]
        self._energized: set[Point] = set()
        self._history: set[Beam] = set()

    def walk(self) -> None:
        """Walk maze by beam from original starting point."""
        return self._walk(initial_beam=Beam(Point(0, -1), RIGHT))

    def find_most_energized(self) -> int:
        """Walk maze from all starting points and find most energized trail."""
        energized_history: list[int] = []
        for initial_beam in self._generate_initial_beams():
            self._energized.clear()
            self._history.clear()
            self._walk(initial_beam)
            energized_history.append(self.energized_count)

        return max(energized_history)

    @property
    def energized_count(self) -> int:
        """Count energized points."""
        return len(self._energized)

    def _walk(self, initial_beam: Beam) -> None:
        """Walk maze by beam."""
        queue = deque([initial_beam])
        while queue:
            beam = queue.popleft()
            if result := self._step(beam):
                queue.extend(result)

    def _step(self, beam: Beam) -> [Beam]:
        """Make single step by beam."""
        next_point = beam.next_point
        new_beam = Beam(next_point, beam.direction)

        if self._is_oob(next_point) or self._already_walked(new_beam):
            return

        self._history.add(new_beam)
        self._energized.add(next_point)

        match val := self._get_value(next_point):
            case '.':
                return [new_beam]
            case '\\' | '/':
                return self._reflect(new_beam, val)
            case '|' | '-':
                return self._split(new_beam, val)
            case _:
                raise ValueError('Unknown value')

    def _get_value(self, p: Point) -> str:
        """Get value of maze."""
        return self._data[p.x][p.y]

    def _is_oob(self, p: Point) -> bool:
        """Check if point is out of bounds."""
        return (p.x < 0 or p.x >= len(self._data)) or (p.y < 0 or p.y >= len(self._data[0]))

    def _already_walked(self, beam: Beam) -> bool:
        """Check if beam already was in history."""
        return beam in self._history

    def _reflect(self, beam: Beam, mirror: str) -> list[Beam]:
        """Reflect beam from mirror."""
        new_direction = MIRRORS_MAP[mirror][beam.direction]
        return [Beam(beam.point, new_direction)]

    def _split(self, beam: Beam, splitter: str) -> list[Beam]:
        """Split beam to one or two beams."""
        return [
            Beam(beam.point, new_direction)
            for new_direction in SPLITTERS_MAP[splitter][beam.direction]
        ]

    def _generate_initial_beams(self) -> Iterator[Beam]:
        """Generate all starting beams for maze."""
        max_x = len(self._data)
        max_y = len(self._data[0])

        for x in range(max_x):
            yield Beam(Point(x, -1), RIGHT)

        for x in range(max_x):
            yield Beam(Point(x, max_y), LEFT)

        for y in range(max_y):
            yield Beam(Point(-1, y), DOWN)

        for y in range(max_y):
            yield Beam(Point(max_x, y), UP)


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    maze = Maze(data)
    maze.walk()
    return maze.energized_count


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    maze = Maze(data)
    return maze.find_most_energized()


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
