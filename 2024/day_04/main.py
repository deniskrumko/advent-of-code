from pathlib import Path
from dataclasses import dataclass
from functools import cached_property

INPUT_FILE = Path(__file__).parent / 'input.txt'


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)


class Puzzle:
    """Class for solving puzzle."""

    def __init__(self, data: str):
        """Initialize class instance."""
        self.data = [list(line) for line in data.splitlines()]

    # Word search

    def count_words(self, word: str = 'XMAS') -> int:
        """Count all words in puzzle."""
        return sum(self.find_word(word, p) for p in self.points)

    def find_word(self, word: str, start: Point) -> int:
        """Find the word in all directions from starting point and count them."""
        return sum(
            word == self.collect_word(start, d, size=len(word))
            for d in self.directions
        )

    def collect_word(self, cur: Point, direction: Point, size: int) -> str:
        """Collect all chars of word in specified direction on puzzle."""
        if size == 0:
            return ''

        val = self.val(cur)
        if not val:
            return ''

        return val + self.collect_word(cur + direction, direction, size - 1)

    # Cross search

    def count_crosses(self, word: str = 'MAS') -> int:
        """Count all crosses in puzzle."""
        return sum(self.has_cross(word, p) for p in self.points)

    def has_cross(self, word: str, point: Point) -> int:
        """Check if block has a cross with required word."""
        len_w = len(word)
        # diagonal from upper-left to bottom-right corner of box
        diagonal_1 = self.collect_word(point, Point(1, 1), size=len_w)
        if not self.is_similar_words(word, diagonal_1):
            return False

        # diagonal from upper-right to bottom-left corner of box
        diagonal_2 = self.collect_word(point + Point(0, len_w - 1), Point(1, -1), size=len_w)
        if not self.is_similar_words(word, diagonal_2):
            return False

        return True

    def is_similar_words(self, word: str, other: str) -> bool:
        """Compare word in both ways."""
        return word == other or word[::-1] == other

    # Internal

    @cached_property
    def total_lines(self) -> int:
        return len(self.data)

    @cached_property
    def total_char_in_line(self) -> int:
        return len(self.data[0])

    @property
    def points(self):
        """Get iterator over all points in puzzle."""
        for i in range(self.total_lines):
            for j in range(self.total_char_in_line):
                yield Point(i, j)

    @property
    def directions(self):
        """Get iterator over all possible directions."""
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == y == 0:
                    continue
                yield Point(x, y)

    def val(self, point: Point) -> str:
        """Get string value of point on puzzle."""
        if not (0 <= point.x < self.total_lines) or not (0 <= point.y < self.total_char_in_line):
            return ''

        return self.data[point.x][point.y]


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    return Puzzle(data).count_words()


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return Puzzle(data).count_crosses()


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
