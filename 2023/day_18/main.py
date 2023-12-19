from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, value: int) -> 'Point':
        return Point(self.x * value, self.y * value)

    def __hash__(self):
        return hash((self.x, self.y))


DIRECTION_NAMES = {'U': Point(-1, 0), 'R': Point(0, 1), 'D': Point(1, 0), 'L': Point(0, -1)}
DIRECTION_NAMES_REV = {v: k for k, v in DIRECTION_NAMES.items()}
PIPES = {
    'R': '-',
    'D': '|',
    'U': '|',
    'L': '-',
}

MMM = {
    'L': {'U': 'L', 'D': 'F'},
    'R': {'U': 'J', 'D': '7'},
    'U': {'L': '7', 'R': 'F'},
    'D': {'L': 'J', 'R': 'L'},
}


@dataclass
class Value:
    point: Point
    corner: str
    direction: str
    steps: int


def dig(commands: list, new_way=False):
    start = Point(0, 0)
    p = start
    prev_dir = None
    result = {p: None}
    first_dir = None
    direction_name = None

    for command in commands:
        direction_name, steps, color = command.split()

        if new_way:
            a, b = color[2:7], color[7:8]
            direction_name = {
                '0': 'R',
                '1': 'D',
                '2': 'L',
                '3': 'U',
            }[b]
            steps = int(a, 16)

        if not first_dir:
            first_dir = direction_name

        corner = ''
        if prev_dir:
            corner = MMM[prev_dir][direction_name]

        steps = int(steps)

        direction = DIRECTION_NAMES[direction_name]
        # value = PIPES[direction_name]

        value = Value(
            point=p,
            corner=corner,
            direction=direction_name,
            steps=steps,
        )

        result[p] = value

        p += (direction * steps)
        prev_dir = direction_name

    if p != start:
        raise ValueError('We did not close the loop')
    else:
        corner = MMM[direction_name][first_dir]
        result[start].corner = corner

    return result


def switch_status(status: int) -> int:
    """Switch boolean status.

    Status means if we are inside or outside of the walked path:
        - 0 = outside
        - 1 = inside

    If we are inside path, we will count the current point to total.
    """
    return (status + 1) % 2


@dataclass
class Range:
    pipe: str
    range_type: str
    fixed_point: int
    range_point: range

    def point_inside(self, point: Point) -> bool:
        if self.range_type == 'x':
            return point.x in self.range_point and point.y == self.fixed_point
        if self.range_type == 'y':
            return point.y in self.range_point and point.x == self.fixed_point
        raise ValueError('/')


def get_range(val):
    newpoint = val.point + DIRECTION_NAMES[val.direction] * val.steps

    match val.direction:
        case 'L':
            return Range(
                pipe='-',
                range_type='y',
                fixed_point=val.point.x,
                range_point=range(newpoint.y, val.point.y),
            )
        case 'R':
            return Range(
                pipe='-',
                range_type='y',
                fixed_point=val.point.x,
                range_point=range(val.point.y, newpoint.y),
            )
        case 'U':
            return Range(
                pipe='|',
                range_type='x',
                fixed_point=val.point.y,
                range_point=range(newpoint.x, val.point.x),
            )
        case 'D':
            return Range(
                pipe='|',
                range_type='x',
                fixed_point=val.point.y,
                range_point=range(val.point.x, newpoint.x),
            )
        case _:
            raise ValueError('..')


def reuse(m: dict):
    min_x = min(p.x for p in m)
    max_x = max(p.x for p in m)
    min_y = min(p.y for p in m)
    max_y = max(p.y for p in m)

    ranges = [get_range(val) for val in m.values()]
    fixed_x_ranges = defaultdict(list)
    fixed_y_ranges = defaultdict(list)

    for ran in ranges:
        if ran.range_type == 'y':  # fixed x
            fixed_x_ranges[ran.fixed_point].append(ran)
        if ran.range_type == 'x':  # fixed y
            fixed_y_ranges[ran.fixed_point].append(ran)

    def detect_value(p: Point):
        nonlocal m
        if p in m:
            return m[p].corner
        else:
            for xran in fixed_x_ranges[p.x]:
                if xran.point_inside(p):
                    return xran.pipe
            for yran in fixed_y_ranges[p.y]:
                if yran.point_inside(p):
                    return yran.pipe

        return '.'

    total = 0
    for x in range(min_x, max_x + 1):
        # print('')
        status = 0
        edge_start = None
        for y in range(min_y, max_y + 1):
            p = Point(x, y)

            value = detect_value(p)
            # print(value, end='')

            if value == '.':
                total += status
                continue
            else:
                total += 1

            match value:
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


def count_area(m: set) -> int:
    """37785 too high"""
    min_x = min(p.x for p in m)
    max_x = max(p.x for p in m)
    min_y = min(p.y for p in m)
    max_y = max(p.y for p in m)

    total = 0
    for x in range(min_x - 1, max_x + 1):
        status = 0
        on_edge = False
        for y in range(min_y - 1, max_y + 1):
            p = Point(x, y)
            if p in m:
                print('#', end='')
                on_edge = True
                total += 1
            else:
                if on_edge:
                    on_edge = False
                    status = (status + 1) % 2

                if status == 0:
                    print('.', end='')
                else:
                    print('@', end='')

                total += status
        print('')
    return total


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    m = dig(data.splitlines())
    return reuse(m)


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    m = dig(data.splitlines(), new_way=True)
    return reuse(m)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
