from libs import Solution, register


@register(day=3, part=1)
class SliceMachinePartOne(Solution):
    """Slice Machine. Part I."""

    data_file = 'inputs/day_03.txt'

    def run(self):
        """Run solution."""
        for value in self.data:
            values = value.split()
            obj_id = int(values[0][1:])
            position = values[2][:-1].split(',')
            size = values[3].split('x')
            import ipdb; ipdb.set_trace(context=8)  # FIXME: Breakpoint


@register(day=3, part=2)
class SliceMachinePartTwo(Solution):
    """Slice Machine. Part II."""

    data_file = 'inputs/day_03.txt'

    def run(self):
        """Run solution."""
        pass
