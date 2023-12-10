from dataclasses import dataclass
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'
START_VALUE = 'S'
EMPTY_VALUE = '.'


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Move:
    fr: Point  # from
    to: Point


@dataclass
class Matrix:
    _data: list[list[str]]

    def get_value(self, p: Point) -> str | None:
        """Get point value on matrix."""
        if self.is_oob(p):  # If point is out of bounds -> no value
            return None

        return self._data[p.x][p.y]

    def set_value(self, p: Point, value: str):
        """Set point value on matrix."""
        self._data[p.x][p.y] = value

    def iter_points(self):
        """Iterate over all points in matrix."""
        for x in range(len(self._data)):
            for y in range(len(self._data[0])):
                yield Point(x, y)

    def is_oob(self, p: Point) -> bool:
        """Check if point is out of bounds."""
        return (p.x < 0 or p.x > len(self._data)) or (p.y < 0 or p.y > len(self._data[0]))

    def get_start_point(self) -> Point:
        """Get starting point from matrix."""
        for p in self.iter_points():
            if self.get_value(p) == START_VALUE:
                return p
        raise ValueError('No starting point in matrix')

    def walk(
        self,
        cur_point: Point,
        cur_value: str,
        prev_move: Point,
    ) -> tuple[Point, str, Point]:
        """Walk one step through matrix and return new point, value and move."""
        to = None
        for move in PIPE_MOVES[cur_value]:
            if move.fr == prev_move:
                to = move.to
                break

        new_point = cur_point + to
        new_val = self.get_value(new_point)
        return new_point, new_val, to


UP, RIGHT, DOWN, LEFT = Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)
PIPE_MOVES = {
    'L': (Move(fr=DOWN, to=RIGHT), Move(fr=LEFT, to=UP)),
    'F': (Move(fr=UP, to=RIGHT), Move(fr=LEFT, to=DOWN)),
    '7': (Move(fr=RIGHT, to=DOWN), Move(fr=UP, to=LEFT)),
    'J': (Move(fr=DOWN, to=LEFT), Move(fr=RIGHT, to=UP)),
    '-': (Move(fr=RIGHT, to=RIGHT), Move(fr=LEFT, to=LEFT)),
    '|': (Move(fr=UP, to=UP), Move(fr=DOWN, to=DOWN)),
}


def parse_data(data: str) -> Matrix:
    """Parse data into matrix."""
    return Matrix(_data=[[v for v in line] for line in data.splitlines()])


def is_allowed_for_start(value: str | None, direction: Point) -> bool:
    """Check if direction is allowed for start point."""
    if value == EMPTY_VALUE or value is None:
        return False

    for move in PIPE_MOVES[value]:
        if move.fr == direction:
            return True
    return False


def replace_start_value(
    matrix: Matrix,
    start_point: Point,
    second_point: Point,
    last_point: Point,
) -> Matrix:
    """Replace start value with correct symbol.

    We need to analyze the direction from start to second point and from last point to start.
    This will give us the correct symbol.
    """
    start_to = second_point - start_point  # Move from start to second point
    start_from = start_point - last_point  # Move from last point to start

    replacement = None
    for symbol, moves in PIPE_MOVES.items():
        for move in moves:
            if move.fr == start_from and move.to == start_to:
                replacement = symbol
                break
        if replacement is not None:
            break

    if replacement is None:
        raise ValueError('No replacement for start value')

    matrix.set_value(start_point, replacement)
    return matrix


def get_first_move(start_point, matrix) -> tuple[Point, str, Point]:
    """Decide first move for start point."""
    for direction in (UP, RIGHT, DOWN, LEFT):
        new_point = start_point + direction
        new_value = matrix.get_value(new_point)
        if is_allowed_for_start(new_value, direction):
            return new_point, new_value, direction
    else:
        raise ValueError('No allowed directions for start point')


def get_walked(matrix) -> tuple[set[Point], Point, Point, Point]:
    """Walk through matrix and return walked points.

    Return:
        walked: set of points that were walked (not ordered)
        start_point: starting point
        second_point: second point from start point
        last_point: last point before returning to start point
    """
    start_point = matrix.get_start_point()
    second_point = None
    last_point = None
    walked: set[Point] = {start_point}

    cur_point, cur_value, prev_move = get_first_move(start_point, matrix)
    second_point = cur_point
    walked.add(cur_point)

    prev_point = None
    while True:
        prev_point = cur_point
        cur_point, cur_value, prev_move = matrix.walk(cur_point, cur_value, prev_move)
        if cur_value == START_VALUE:
            last_point = prev_point
            break
        else:
            walked.add(cur_point)

    return walked, start_point, second_point, last_point


def switch_status(status: int) -> int:
    """Switch boolean status.

    Status means if we are inside or outside of the walked path:
        - 0 = outside
        - 1 = inside

    If we are inside path, we will count the current point to total.
    """
    return (status + 1) % 2


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    matrix = parse_data(data)
    walked = get_walked(matrix)[0]
    return int(len(walked) / 2)


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    matrix = parse_data(data)
    walked, start_point, second_point, last_point = get_walked(matrix)
    matrix = replace_start_value(matrix, start_point, second_point, last_point)

    total = 0
    for p in matrix.iter_points():
        if p.y == 0:
            status = 0
            edge_start = None

        # Count points inside path (if status is 1)
        if p not in walked:
            total += status
            continue

        match value := matrix.get_value(p):
            case '|':  # hit wall -> switch status
                status = switch_status(status)
            case '-':  # walking on pipe
                continue
            case 'L' | 'F':  # hit flat corner -> start walking on pipe
                edge_start = value
            case '7' | 'J':  # hit shart corner -> get off the pipe -> optionally switch status
                if edge_start == 'L' and value == '7':
                    status = switch_status(status)
                if edge_start == 'F' and value == 'J':
                    status = switch_status(status)
            case _:
                raise ValueError(f'undefined value: {value}')

    return total


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
