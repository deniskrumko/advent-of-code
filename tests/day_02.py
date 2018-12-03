from libs import TestCase, register


@register(day=2, part=1, is_test=True)
class TestInventoryManagementSystemPartOne(TestCase):
    """Tests for ``InventoryManagementSystemPartOne``."""

    def run(self):
        """Run tests."""
        data = (
            'abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab',
        )
        assert self.solution_class(data).run() == 12


@register(day=2, part=2, is_test=True)
class TestInventoryManagementSystemPartTwo(TestCase):
    """Tests for ``InventoryManagementSystemPartTwo``."""

    def run(self):
        """Run tests."""
        data = (
            'abcde',
            'fghij',
            'klmno',
            'pqrst',
            'fguij',
            'axcye',
            'wvxyz',
        )
        assert self.solution_class(data).run() == 'fgij'
