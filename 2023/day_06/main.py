import math
import re
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def parse_data(data: str):
    """Parse initial data."""
    match = re.match(r'^Time:(?P<times>.+)\nDistance:(?P<distances>.+)$', data).groupdict()
    return match['times'], match['distances']


def count_winning_v1(t_allowed: int, d_record: int) -> int:
    """Bruteforcing winning cases. This is slow 🐢"""
    wining_cases = 0
    for t_hold in range(t_allowed):
        t_remain = t_allowed - t_hold
        d_current = t_hold * t_remain
        wining_cases += d_current > d_record
    return wining_cases


def count_winning_v2(t_allowed: int, d_record: int) -> int:
    """Calculating result using math. Math is cool 😎"""
    def _floor(x):
        # Custom floor finds prev integer: 5.1 -> 5 and 5.0 -> 4
        return int(x) - ((x - int(x)) == 0)

    def _ceil(x):
        # Custom ceil finds next integer: 5.1 -> 6 and 5.0 -> 6
        return int(x) + 1

    # Solve quadratic equation
    a, b, c = 1, -t_allowed, d_record
    D = pow(b, 2) - (4 * a * c)
    x1, x2 = (-b - math.sqrt(D)) / 2, (-b + math.sqrt(D)) / 2

    # Swap if points are reversed
    if x1 > x2:
        x1, x2 = x2, x1

    # Count all integer values between x1 and x2
    return _floor(x2) - _ceil(x1) + 1


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1, original solution, slow)."""
    times, distances = map(lambda line: [int(v) for v in line.split()], parse_data(data))
    return math.prod(count_winning_v1(times[i], distances[i]) for i in range(len(times)))


def function_1a(data: str) -> bool:
    """Get result for puzzle (part 1, updated solution, fast)."""
    times, distances = map(lambda line: [int(v) for v in line.split()], parse_data(data))
    return math.prod(count_winning_v2(times[i], distances[i]) for i in range(len(times)))


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2, original solution, slow)."""
    t_allowed, d_record = map(lambda line: int(line.replace(' ', '')), parse_data(data))
    return count_winning_v1(t_allowed, d_record)


def function_2a(data: str) -> bool:
    """Get result for puzzle (part 2, updated solution, fast)."""
    t_allowed, d_record = map(lambda line: int(line.replace(' ', '')), parse_data(data))
    return count_winning_v2(t_allowed, d_record)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
