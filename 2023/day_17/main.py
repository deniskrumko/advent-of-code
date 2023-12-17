from collections import deque
from dataclasses import dataclass
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'
DIRECTION_NAMES = {'UP': (-1, 0), 'RIGHT': (0, 1), 'DOWN': (1, 0), 'LEFT': (0, -1)}
DIRECTION_NAMES_REV = {v: k for k, v in DIRECTION_NAMES.items()}


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: 'Direction') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))


class Direction(Point):

    @classmethod
    def from_difference(cls, prev_point, next_point):
        """DOCS"""
        return cls(next_point.x - prev_point.x, next_point.y - prev_point.y)

    @property
    def opposite(self) -> 'Direction':
        return Direction(x=self.x * -1, y=self.y * -1)

    def __repr__(self) -> str:
        return DIRECTION_NAMES_REV[(self.x, self.y)]


ALL_DIRECTIONS = [Direction(x=move[0], y=move[1]) for move in DIRECTION_NAMES.values()]


@dataclass
class Walker:
    point: Point
    trail: list[Point]
    heat: int = 0

    @classmethod
    def generate_new_walker(cls, w: 'Walker', new_point: Point, accumulated_heat: int):
        return cls(point=new_point, trail=w.trail + [w.point], heat=accumulated_heat)

    def already_walked(self, p: Point) -> bool:
        return p in self.trail

    @property
    def last_direction(self) -> Direction | None:
        result = self.get_n_last_directions(1)
        return result[0] if result else None

    @property
    def three_last_directions(self) -> list[Direction] | None:
        return self.get_n_last_directions(3)

    @property
    def steps(self) -> list[Direction]:
        return self.get_n_last_directions(len(self.trail))

    def get_n_last_directions(self, n: int) -> list[Direction] | None:
        if len(self.trail) < n:
            return None

        path = self.trail[-n:] + [self.point]
        return [Direction.from_difference(path[i], path[i + 1]) for i in range(n)]

    def __repr__(self) -> str:
        return f'<Walker ({self.heat}): {"".join(repr(s)[0] for s in self.steps)}>'


class Maze:

    def __init__(self, data: str):
        self._data = [[int(ch) for ch in line] for line in data.splitlines()]
        self._heat_history: dict[Point, int] = {}
        self._to_kill = set()

    @property
    def max_x(self):
        return len(self._data) - 1

    @property
    def max_y(self):
        return len(self._data[0]) - 1

    def walk(self) -> int:
        """Walk maze and find minimal heat loss track."""
        start_point = Point(0, 0)
        start_point_heat = self.get_heat_value(start_point)
        end_point = Point(self.max_x, self.max_y)
        queue = deque([Walker(point=start_point, trail=[], heat=start_point_heat)])

        results = []
        while queue:
            w = queue.popleft()

            for direction in self.where_to_go(w):
                new_point = self.step(w.point, direction)
                if self.is_oob(new_point) or w.already_walked(new_point):
                    continue

                new_point_heat = self.get_heat_value(new_point)
                accumulated_heat = new_point_heat + w.heat

                # three_last = (w.get_n_last_directions(2) or w.trail) + [direction]
                min_p_heat = self.get_min_heat(new_point) or 100
                if accumulated_heat < min_p_heat:
                    self.set_min_heat(new_point, accumulated_heat)
                    self.kill_others(new_point, accumulated_heat, queue)
                elif self.kill_myself(accumulated_heat, min_p_heat):
                    continue

                if new_point == end_point:
                    results.append(accumulated_heat - start_point_heat)
                    continue

                # move is valid - ok
                queue.append(Walker.generate_new_walker(w, new_point, accumulated_heat))

        return min(results)

    def kill_myself(self, accumulated_heat, min_p_heat):
        tr = 5
        return (accumulated_heat - min_p_heat) > tr

    def kill_others(self, new_point, new_min_heat, queue):
        will_be_killed = []
        for walker in queue:
            if new_point in walker.trail:
                trail_heat = self.calculate_trail_heat(walker.trail)
                if self.kill_myself(trail_heat, new_min_heat):
                    will_be_killed.append(walker)

        for walker in will_be_killed:
            queue.remove(walker)

    def calculate_trail_heat(self, trail: list[Point]) -> int:
        return sum(self.get_heat_value(p) for p in trail)

    def step(self, p: Point, direction: Direction) -> Point:
        return p + direction

    def where_to_go(self, w: Walker) -> list[Direction]:
        """Decide where to go based on walked trail and last directions."""
        last_direction = w.last_direction
        if last_direction is None:
            return ALL_DIRECTIONS

        possible = [d for d in ALL_DIRECTIONS if d != last_direction.opposite]

        three_last = w.three_last_directions
        if three_last and self.is_straight_line(three_last):
            possible.remove(last_direction)

        return possible

    def get_heat_value(self, p: Point) -> int:
        return self._data[p.x][p.y]

    def get_min_heat(self, p: Point) -> int | None:
        # key = hash(f'{p}.{last_directions}')
        return self._heat_history.get(p)

    def set_min_heat(self, p: Point, heat: int) -> None:
        # key = hash(f'{p}.{last_directions}')
        self._heat_history[p] = heat

    def is_straight_line(self, directions: list[Direction]) -> bool:
        if len(directions) < 2:
            raise ValueError('Not enough data')

        return len(set(directions)) == 1

    def is_oob(self, p: Point) -> bool:
        """Check if point is out of bounds."""
        return (p.x < 0 or p.x >= len(self._data)) or (p.y < 0 or p.y >= len(self._data[0]))


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    maze = Maze(data)
    return maze.walk()


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return True


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
