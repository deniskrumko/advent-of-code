from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

INPUT_FILE = Path(__file__).parent / 'input.txt'


@dataclass
class Rule:
    """Rule class."""

    left: int
    right: int

    @classmethod
    def parse(cls, line: str) -> 'Rule':
        """Parse rule from string."""
        left, right = line.split('|')
        return cls(left=int(left), right=int(right))

    def contains(self, value: int) -> bool:
        """Check if rule contains value."""
        return self.left == value or self.right == value


@dataclass
class Page:
    """Page class."""

    values: list[int]

    @classmethod
    def parse(cls, line: str) -> 'Page':
        """Parse page from string."""
        page = cls(values=list(map(int, line.split(','))))

        # No duplicates allowed because it will brake index() calls
        if len(page.values) != len(set(page.values)):
            raise ValueError('page contains duplicates')

        return page

    @property
    def middle_value(self):
        """Get middle value of page."""
        if len(self.values) % 2 != 1:
            raise ValueError('page values must be odd')

        return self.values[len(self.values) // 2]

    def contains(self, rule: Rule) -> bool:
        """Check if page contains rule."""
        return rule.left in self.values and rule.right in self.values

    def is_valid(self, rules: list[Rule]) -> bool:
        """Check if page is valid by specified rules."""
        for value in self.values:
            for rule in rules:
                if rule.contains(value) and self.contains(rule):
                    li, ri = self.values.index(rule.left), self.values.index(rule.right)
                    if li > ri:
                        return False

        return True

    def sort_values(self, rules: list[Rule]):
        """Sort page values by specified rules."""
        for value in self.values:
            for rule in rules:
                if rule.contains(value) and self.contains(rule):
                    li, ri = self.values.index(rule.left), self.values.index(rule.right)
                    if li > ri:
                        # insert left value before right
                        self.values.remove(rule.left)
                        self.values.insert(ri, rule.left)
                        return self.sort_values(rules)

        if not self.is_valid(rules):
            raise ValueError('sorting does not work')


@dataclass
class Puzzle:
    """Puzzle class."""

    rules: list[Rule]
    pages: list[Page]

    @classmethod
    def parse(cls, data: str) -> 'Puzzle':
        """Parse puzzle from string."""
        rules, pages = data.split('\n\n')
        return cls(
            rules=[Rule.parse(line) for line in rules.split()],
            pages=[Page.parse(line) for line in pages.splitlines()],
        )

    def get_pages(self, valid: bool) -> Iterable[Page]:
        """Get all valid pages."""
        for page in self.pages:
            if page.is_valid(self.rules) == valid:
                yield page

    def fix_page(self, page: Page) -> Page:
        """Fix page ordering."""
        page.sort_values(rules=self.rules)
        return page


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    puzzle = Puzzle.parse(data)
    valid_pages = puzzle.get_pages(valid=True)
    return sum(p.middle_value for p in valid_pages)


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    puzzle = Puzzle.parse(data)
    invalid_pages = puzzle.get_pages(valid=False)
    fixed_pages = (puzzle.fix_page(p) for p in invalid_pages)
    return sum(p.middle_value for p in fixed_pages)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
