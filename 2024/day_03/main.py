import re
from dataclasses import dataclass
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'
REGEXP_PATTERN = r'mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)'
DO, DONT = "do()", "don't()"


@dataclass
class Mul:
    a: str
    b: str

    def eval(self) -> int:
        return int(self.a) * int(self.b)


@dataclass
class MulList:
    values: list[Mul]

    @classmethod
    def from_str(cls, line: str) -> 'MulList':
        """Find all ``Mul`` objects in string using regex."""
        return cls(values=[
            Mul(**m.groupdict())
            for m in re.compile(REGEXP_PATTERN).finditer(line)
        ])

    @property
    def total(self) -> int:
        """Total sum of all ``Mul`` objects."""
        return sum(v.eval() for v in self.values)


def make_valid_line(data: str, enabled: bool = True) -> str:
    """Make a valid line out of line with invalid parts."""
    if enabled:
        try:
            i = data.index(DONT)
        except ValueError:
            return data  # if no "don't()" in current line -> whole line is valid

        left, right = data[:i], data[i + len(DONT):]
        return left + make_valid_line(right, enabled=False)
    else:
        try:
            i = data.index(DO)
        except ValueError:
            return ''  # if no "do()" in current line -> whole line is invalid

        right = data[i + len(DO):]  # left part is invalid, so skip it
        return make_valid_line(right, enabled=True)


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    return sum(MulList.from_str(line).total for line in data.splitlines())


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return function_1(data=make_valid_line(data))


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
