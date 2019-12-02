from libs import TestCase, register


@register(day=3, part=1, is_test=True)
class TestDay3Part1(TestCase):
    """Tests for ``InventoryManagementSystemPartOne``."""

    def run(self):
        """Run tests."""
        data = (
            '#1 @ 1,3: 4x4',
            '#2 @ 3,1: 4x4',
            '#3 @ 5,5: 2x2',
        )
        assert self.solution_class(data).run() == 4
