class HexMap(object):
    """Docstring"""

    sides = ['n', 'ne', 'se', 's', 'sw', 'nw']

    def __init__(self, path):
        """Custom `__init__` method."""
        self.path = path.split(',')

    def get_opposite(self, step):
        current_index = self.sides.index(step)
        return self.sides[(current_index + 3) % 6]

    def get_sides(self, step):
        current_index = self.sides.index(step)
        left = self.sides[(current_index - 2) % 6]
        right = self.sides[(current_index + 2) % 6]
        return left, right

    def get_middle_left(self, step):
        current_index = self.sides.index(step)
        return self.sides[(current_index - 1) % 6]

    def get_middle_right(self, step):
        current_index = self.sides.index(step)
        return self.sides[(current_index + 1) % 6]

    def count_steps(self):
        self.max_distance = 0

        while True:
            saved = []
            for step in self.path:

                if len(saved) > self.max_distance:
                    self.max_distance = len(saved)

                if not saved:
                    saved.append(step)
                    continue

                opposite = self.get_opposite(step)
                if opposite in saved:
                    saved.remove(opposite)
                    continue

                left, right = self.get_sides(step)
                if left in saved:
                    saved.remove(left)
                    saved.append(self.get_middle_left(step))
                    continue

                if right in saved:
                    saved.remove(right)
                    saved.append(self.get_middle_right(step))
                    continue

                saved.append(step)

            if self.path == saved:
                return len(saved)

            self.path = saved


if __name__ == '__main__':
    tests = {
        'ne,ne,ne': 3,
        'ne,ne,sw,sw': 0,
        'ne,ne,s,s': 2,
        'se,sw,se,sw,sw': 3
    }

    for test, result in tests.items():
        assert HexMap(test).count_steps() == result, test

    with open('day11/input.txt', 'r') as f:
        puzzle = f.readline().replace('\n', '')

    hex_map = HexMap(puzzle)

    print(hex_map.count_steps())
    print(hex_map.max_distance)
