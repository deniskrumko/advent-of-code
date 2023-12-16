from dataclasses import dataclass
from pathlib import Path

import pandas as pd

INPUT_FILE = Path(__file__).parent / 'input.txt'
ROCK, GROUND, WALL = 'O', '.', '#'


@dataclass
class Puzzle:
    """Class for storing puzzle map."""

    def __init__(self, data: str):
        self.df = pd.DataFrame([[ch for ch in line] for line in data.splitlines()])

    def tilt_north(self) -> 'Puzzle':
        """Tilt map to north edge."""
        self.df = self._tilt(self.df.copy())
        return self

    def cycle_tilt(self, cycles: int) -> 'Puzzle':
        """Tilt map to all edges N times."""
        self.df = self._cycle_tilt(cycles, self.df)
        return self

    @property
    def load(self):
        """Count sum load to north edge."""
        result = 0
        max_len = len(self.df)
        for i in self.df:
            for value in self.df.iloc[i]:
                if value == ROCK:
                    result += max_len - i

        return result

    def _cycle_tilt(self, cycles: int, df: pd.DataFrame) -> pd.DataFrame:
        """Perform cycle of tilts to dataframe N times."""
        df_history = {}
        cycles_history = {}
        inverted_cycles_history = {}
        for i in range(cycles):
            for _ in range(4):
                df = self._tilt(df)
                df = self._rotate(df)

            df_hash = sum(pd.util.hash_pandas_object(df))
            if df_hash in df_history:
                left_boundary = cycles_history[df_hash]
                ex_stage = left_boundary + (cycles - left_boundary) % (i - left_boundary) - 1
                df_hash_history = inverted_cycles_history[ex_stage]
                return df_history[df_hash_history]
            else:
                df_history[df_hash] = df.copy()
                cycles_history[df_hash] = i
                inverted_cycles_history[i] = df_hash

        return df

    def _rotate(self, df):
        """Rotate board clockwise 1 time."""
        return pd.DataFrame([[v for v in df[i][::-1]] for i in df])

    def _tilt(self, df) -> pd.DataFrame:
        """Tilt dataframe to north edge to move rocks."""
        for i in df:
            new_v_line = ''
            for group in ''.join(df[i]).split(WALL):
                rocks = group.count(ROCK)
                new_v_line += (ROCK * rocks + GROUND * (len(group) - rocks) + WALL)

            df[i] = pd.Series([x for x in new_v_line[:len(df)]])

        return df


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    return Puzzle(data).tilt_north().load


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return Puzzle(data).cycle_tilt(1000000000).load


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
