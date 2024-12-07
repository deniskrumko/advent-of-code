import time
from dataclasses import dataclass
from functools import wraps
from itertools import product
from pathlib import Path
from typing import (
    Any,
    Callable,
)

INPUT_FILE = Path(__file__).parent / 'input.txt'
ADD, MUL, CONCAT = '+', '*', '||'


def timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        time_start = time.monotonic()
        result = func(*args, **kwargs)
        time_end = time.monotonic()
        print(f'Operation done in {time_end - time_start:.2f} seconds')
        return result
    return wrapper


@dataclass
class Equation:
    result: int
    values: tuple[int]

    @classmethod
    def from_str(cls, line: str) -> 'Equation':
        """Initialize equation fro string."""
        result, values = line.split(':')
        return cls(
            result=int(result),
            values=tuple(int(v) for v in values.split()),
        )

    def is_possible(self, allowed_operators: list[str]) -> int:
        """Check if equation is possible by allowed operators."""
        for instruction in product(allowed_operators, repeat=len(self.values) - 1):
            total = self.values[0]

            for i, operator in enumerate(instruction):
                next_val = self.values[i + 1]
                if operator == ADD:
                    total += next_val
                elif operator == MUL:
                    total *= next_val
                elif operator == CONCAT:
                    total = int(str(total) + str(next_val))

                if total > self.result:
                    break

            if total == self.result:
                return self.result

        return 0


def count_possible(data: str, *allowed_operators: tuple[str]) -> int:
    """Count all possible equations."""
    return sum(
        Equation.from_str(line).is_possible(allowed_operators)
        for line in data.splitlines()
    )


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    return count_possible(data, ADD, MUL)


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2).

    Not optimal solution. Anyway...
    """
    return count_possible(data, ADD, MUL, CONCAT)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {timer(function_1)(input_data)}')
        print(f'Your result (2): {timer(function_2)(input_data)}')
