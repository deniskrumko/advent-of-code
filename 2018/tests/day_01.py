from libs import (
    TestCase,
    register,
)


@register(day=1, part=1, is_test=True)
class TestChronalCalibrationPartOne(TestCase):
    """Tests for ``ChronalCalibrationPartOne``."""

    def run(self):
        """Run tests."""
        self.check('+1, +1, +1', 3)
        self.check('+1, +1, -2', 0)
        self.check('-1, -2, -3', -6)

    def check(self, string, value):
        """Check expected result."""
        data = string.split(',')
        assert self.solution_class(data).run() == value


@register(day=1, part=2, is_test=True)
class TestChronalCalibrationPartTwo(TestCase):
    """Tests for ``ChronalCalibrationPartTwo``."""

    def run(self):
        """Run tests."""
        self.check('+1, -1', 0)
        self.check('+3, +3, +4, -2, -4', 10)
        self.check('-6, +3, +8, +5, -6', 5)
        self.check('+7, +7, -2, -7, -4', 14)

    def check(self, string, value):
        """Check expected result."""
        data = string.split(',')
        assert self.solution_class(data).run() == value
