from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'
EMPTY, CRATE, CUSTOM_CRATE, OOB = '.', '#', '@', '*'

DOWN, RIGHT, UP, LEFT = 'v', '>', '^', '<'
ROTATIONS = [UP, RIGHT, DOWN, LEFT, UP]


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))


DIRECTIONS = {
    DOWN: Point(1, 0),
    RIGHT: Point(0, 1),
    UP: Point(-1, 0),
    LEFT: Point(0, -1),
}
DIRECTIONS_INVERT = {v: k for k, v in DIRECTIONS.items()}


@dataclass
class Guard:
    pos: Point
    direct: Point
    walked: set[Point]
    on_same_path: int = 0

    @classmethod
    def guard_or_not(cls, pos: Point, val: str) -> 'Guard | None':
        """Initialize guard instance if value is correct."""
        if (direct := DIRECTIONS.get(val)):
            return cls(pos=pos, direct=direct, walked={pos})

    @property
    def next_step(self) -> Point:
        return self.pos + self.direct

    def rotate(self):
        """Rotate by -90 degrees."""
        direct_str = DIRECTIONS_INVERT[self.direct]
        next_direct = ROTATIONS[ROTATIONS.index(direct_str) + 1]
        self.direct = DIRECTIONS[next_direct]

    def step(self) -> None:
        """Make a step."""
        self.prev_pos = self.pos
        self.pos = self.next_step

        if self.pos in self.walked:
            self.on_same_path += 1
        else:
            self.walked.add(self.pos)
            self.on_same_path = 0

    def stuck_in_loop(self, size: int) -> bool:
        return self.on_same_path >= size


class Puzzle:
    """Class for solving puzzle."""

    def __init__(self, data: str):
        """Initialize class instance."""
        self.data = [list(line) for line in data.splitlines()]

    def walk_guard(self, guard: Guard) -> int:
        """Walk guard by the puzzle map.

        Return 1 if guard stuck in loop, 0 if he walked out of maze.
        """
        while True:
            val = self.val(guard.next_step)
            if val == OOB:
                return 0
            elif val in (CRATE, CUSTOM_CRATE):
                guard.rotate()
            else:
                guard.step()

            if guard.stuck_in_loop(size=self.total_lines):
                return 1

    def find_guard(self) -> Guard:
        """Find guard on map."""
        for p in self.points:
            if (guard := Guard.guard_or_not(p, self.val(p))):
                self.data[p.x][p.y] = EMPTY
                return guard

        raise ValueError('guard not found')

    def with_crate(self, pos: Point) -> 'Puzzle':
        self.data[pos.x][pos.y] = CUSTOM_CRATE
        return self

    def print_map(self, guard: Guard):
        """Print map."""
        for i in range(self.total_lines):
            for j in range(self.total_char_in_line):
                p = Point(i, j)
                val = self.val(p)
                if guard.pos == p:
                    val = DIRECTIONS_INVERT[guard.direct]
                elif p in guard.walked:
                    val = 'X'

                print(val, end='')
            print()

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


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    puzzle = Puzzle(data)
    guard = puzzle.find_guard()

    if puzzle.walk_guard(guard) == 1:
        raise ValueError('guard stuck in loop')

    return len(guard.walked)


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2).

    Not optimal solution. Anyway...
    """
    original_puzzle = Puzzle(data)
    original_guard = original_puzzle.find_guard()
    start_position, start_direct = original_guard.pos, original_guard.direct
    original_puzzle.walk_guard(original_guard)

    stuck_pos = set()
    for pos in original_guard.walked:
        if pos == start_position:
            continue  # crate can't be placed at starting position

        # Create new maze with new crate
        puzzle = Puzzle(data).with_crate(pos)

        # Walk the guard and see if he stuck
        guard = Guard(pos=start_position, direct=start_direct, walked={start_position})
        if puzzle.walk_guard(guard):
            stuck_pos.add(pos)

    return len(stuck_pos)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
