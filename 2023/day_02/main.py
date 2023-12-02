import math
from dataclasses import dataclass
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'
CUBES_DICT = {'red': 12, 'green': 13, 'blue': 14}


@dataclass
class Game:
    line: str

    def cubes_iter(self):
        for cube_sets in self.line.split(':')[1].split(';'):
            for cube_set in cube_sets.split(','):
                num, color = cube_set.strip().split()
                yield color, int(num)

    @property
    def is_possible(self) -> bool:
        for color, num in self.cubes_iter():
            if num > CUBES_DICT[color]:
                return False
        return True

    @property
    def power(self) -> int:
        cube_maxes = {}
        for color, num in self.cubes_iter():
            if color not in cube_maxes or num > cube_maxes[color]:
                cube_maxes[color] = num
        return math.prod(cube_maxes.values())


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    return sum(
        i if Game(line).is_possible else 0
        for i, line in enumerate(data.splitlines(), start=1)
    )


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return sum(Game(line).power for line in data.splitlines())


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
