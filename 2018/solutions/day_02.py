from collections import Counter
from functools import reduce

from libs import (
    Solution,
    register,
)


@register(day=2, part=1)
class InventoryManagementSystemPartOne(Solution):
    """Inventory Management System. Part I."""

    data_file = 'inputs/day_02.txt'

    def run(self):
        """Run solution."""
        results = {2: 0, 3: 0}

        for value in self.data:
            counter = Counter(value.strip())
            for key in results:
                results[key] += key in counter.values()

        return results[2] * results[3]


@register(day=2, part=2)
class InventoryManagementSystemPartTwo(Solution):
    """Inventory Management System. Part II."""

    data_file = 'inputs/day_02.txt'

    def run(self):
        """Run solution.

        Get pair of two strings that differ only by 1 char and return common
        characters.

        """
        a, b = self.get_pair()
        return self.get_common(a, b)

    def get_pair(self):
        """Get pair of similar string."""
        for a in self.data:
            for b in self.data:
                if a != b and self.check_difference(a, b):
                    return a, b

    def check_difference(self, a, b):
        """Check that two strings differ only by 1 character in same place."""
        return reduce(lambda x, y: x + (y[0] != y[1]), zip(a, b), 0) == 1

    def get_common(self, a, b):
        """Get string of common characters between two similar strings."""
        return ''.join(x for x, y in zip(a, b) if x == y)
