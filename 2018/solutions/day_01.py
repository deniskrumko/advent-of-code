from itertools import cycle

from libs import Solution, register


@register(day=1, part=1)
class ChronalCalibrationPartOne(Solution):
    """Chronal calibration. Part I."""

    data_file = 'inputs/day_01.txt'

    def run(self):
        """Get sum of all values."""
        return sum(int(value) for value in self.data)


@register(day=1, part=2)
class ChronalCalibrationPartTwo(Solution):
    """Chronal calibration. Part II."""

    data_file = 'inputs/day_01.txt'

    def run(self):
        """Get first occurency of repeated frequency."""
        current = 0
        items = {current}

        for value in cycle(self.data):
            current += int(value)
            if current in items:
                return current

            items.add(current)
