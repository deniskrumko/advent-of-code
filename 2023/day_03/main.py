import math
import re
from dataclasses import dataclass
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


@dataclass
class Value:
    """Base class for values."""

    value: str
    start: tuple
    end: tuple
    _regexp = ''

    @classmethod
    def findall(cls, i: int, line: str):
        """Find all value occurencies in line."""
        for m in re.compile(cls._regexp).finditer(line):
            yield cls(value=m.group(), start=(i, m.start()), end=(i, m.end() - 1))


class Symbol(Value):
    """Class for symbols."""

    _regexp = r'[^0-9.]'

    def is_gear(self, numbers) -> int:
        """Check if symbol is a gear.

        Returns gear ratio if it's a gear, otherwise - 0.
        """
        if self.value != '*':
            return 0

        adjacent_numbers = [n for n in numbers if n.is_adjacent(self)]
        if len(adjacent_numbers) != 2:
            return 0

        return math.prod(int(n.value) for n in adjacent_numbers)


class Number(Value):
    """Class for numbers."""

    _regexp = r'\d+'

    def is_adjacent(self, s: Symbol) -> bool:
        """Check if Number is adjacent to a Symbol."""
        X = (self.start[0] - 1, self.start[1] - 1)
        Y = (self.end[0] + 1, self.end[1] + 1)
        return (X[0] <= s.start[0] <= Y[0]) and (X[1] <= s.start[1] <= Y[1])


def parse_data(data: str):
    """Find numbers and symbols in puzzle data."""
    numbers, symbols = [], []
    for i, line in enumerate(data.splitlines(), 0):
        numbers.extend(Number.findall(i, line))
        symbols.extend(Symbol.findall(i, line))
    return numbers, symbols


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    numbers, symbols = parse_data(data)
    return sum(int(n.value) for n in numbers if any(n.is_adjacent(s) for s in symbols))


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    numbers, symbols = parse_data(data)
    return sum(s.is_gear(numbers) for s in symbols)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
