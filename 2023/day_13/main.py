from dataclasses import dataclass
from pathlib import Path

import pandas as pd

INPUT_FILE = Path(__file__).parent / 'input.txt'


@dataclass
class Puzzle:
    def __init__(self, data: list[list[str]]):
        self.df = pd.DataFrame(data)

    def get_ver_reflection(self, smudge_fix: bool) -> int:
        return self.__find_reflection_index(self.df, smudge_fix)

    def get_hor_reflection(self, smudge_fix: bool) -> int:
        return self.__find_reflection_index(self.df.T, smudge_fix)

    def __find_reflection_index(self, df: pd.DataFrame, smudge_fix: bool) -> int:
        max_values, max_lines = df.shape
        for i in range(max_lines - 1):
            fixed = False
            is_mirrored = True
            for x in range(i, -1, -1):
                mirrored_index = (i - x) + 1
                if mirrored_index + i >= max_lines:  # too far to right
                    continue

                comp = df[x] == df[i + mirrored_index]
                if not comp.all():
                    # if lines are different by exactly 1 element -> try to fix
                    if smudge_fix and not fixed and comp.sum() == max_values - 1:
                        fixed = True
                        continue
                    is_mirrored = False
                    break

            if is_mirrored:
                if not smudge_fix or (smudge_fix and fixed):
                    return i + 1

        return 0


def parse_data(data: str) -> list[Puzzle]:
    """Parse puzzle data."""
    return [
        Puzzle([[ch for ch in line] for line in section.splitlines()])
        for section in data.split('\n\n')
    ]


def function_1(data: str, smudge_fix: bool = False) -> bool:
    """Get result for puzzle (part 1)."""
    puzzles = parse_data(data)
    return sum(
        p.get_hor_reflection(smudge_fix) * 100 + p.get_ver_reflection(smudge_fix)
        for p in puzzles
    )


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return function_1(data, smudge_fix=True)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
