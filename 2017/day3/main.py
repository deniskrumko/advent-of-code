
class ManhattanDistance(object):
    """Class for calculation of manhattan distance for spiral stored numbers"""

    def __init__(self, number):
        self.result = self.get_manhattan_distance(number)

    def get_ring(self, number):
        """Get ring for provided number."""
        ring = 0
        ring_base = 1

        while True:
            if number <= pow(ring_base, 2):
                return ring

            ring_base += 2
            ring += 1

    def get_ring_root(self, ring):
        return pow(ring * 2 + 1, 2)

    def get_ring_root_coordinated(self, ring):
        return (ring, -ring)

    def get_coordinates_sum(self, a, b):
        return (a[0] + b[0], a[1] + b[1])

    def get_ring_side(self, ring):
        return ring * 2 + 1

    def get_adder(self, adder_index):
        adders = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        return adders[adder_index % 4]

    def get_manhattan_distance(self, puzzle_number):
        ring = self.get_ring(puzzle_number)
        ring_side = self.get_ring_side(ring)

        coordinates = self.get_ring_root_coordinated(ring)
        number = self.get_ring_root(ring)
        adder_index = 0
        adder = self.get_adder(adder_index)
        steps = 0

        while True:
            if puzzle_number == number:
                break

            coordinates = self.get_coordinates_sum(coordinates, adder)

            steps += 1
            number -= 1

            if steps % (ring_side - 1) == 0 and steps != 0:
                adder_index += 1
                adder = self.get_adder(adder_index)

        return abs(coordinates[0]) + abs(coordinates[1])


class AdjacentSquares(object):

    def __init__(self, end_number):
        """Initialization method."""
        self.end_number = end_number
        self.spiral = {}
        self.number = 1
        self.coordinates = (0, 0)

        self.result = self.build_spiral()

    def get_coordinates_sum(self, a, b):
        return (a[0] + b[0], a[1] + b[1])

    def coord(self, direction):
        direction_map = {
            'up': (self.coordinates[0], self.coordinates[1] + 1),
            'down': (self.coordinates[0], self.coordinates[1] - 1),
            'left': (self.coordinates[0] - 1, self.coordinates[1]),
            'right': (self.coordinates[0] + 1, self.coordinates[1]),
        }
        return direction_map[direction]

    def check_coordinates(self, *args):
        directions = set(['up', 'down', 'left', 'right'])
        existing = set(args)
        not_existing = directions - existing

        for direction in existing:
            coordinate = self.coord(direction)
            if not self.spiral.get(coordinate, None):
                return False

        for direction in not_existing:
            coordinate = self.coord(direction)
            if self.spiral.get(coordinate, None):
                return False

        return True

    def get_direction(self):
        if self.check_coordinates('left'):
            return 'up'

        if self.check_coordinates('left', 'down'):
            return 'up'

        if self.check_coordinates('down'):
            return 'left'

        if self.check_coordinates('right', 'down'):
            return 'left'

        if self.check_coordinates('right'):
            return 'down'

        if self.check_coordinates('right', 'up'):
            return 'down'

        if self.check_coordinates('up'):
            return 'right'

        if self.check_coordinates('up', 'left'):
            return 'right'

        return 'right'

    def get_adjacent_sum(self):
        result_sum = 0

        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == j == 0:
                    continue

                coord = self.get_coordinates_sum(self.coordinates, (i, j))
                number = self.spiral.get(coord, None)
                if number:
                    result_sum += number

        return result_sum

    def end_condition(self):
        return self.number > self.end_number

    def build_spiral(self):
        self.spiral[self.coordinates] = self.number

        while True:
            direction = self.get_direction()
            self.coordinates = self.coord(direction)
            self.number = self.get_adjacent_sum()
            self.spiral[self.coordinates] = self.number

            if self.end_condition():
                return self.number


class ManhattanDistance2(AdjacentSquares):
    def get_adjacent_sum(self):
        return self.number + 1

    def end_condition(self):
        return self.number == self.end_number

    def build_spiral(self):
        super().build_spiral()
        return abs(self.coordinates[0]) + abs(self.coordinates[1])


def main():
    with open('day3/input.txt', 'r') as f:
        puzzle = int(f.readline())

    distance = ManhattanDistance(puzzle).result
    adjacent = AdjacentSquares(puzzle).result
    print('Manhattan distance: {0}'.format(distance))
    print('Adjacent: {0}'.format(adjacent))

    print('\nCalculation of manhattan distance\n')
    print('In this time program builds spiral with {} numbers'.format(puzzle))
    print('It takes a while...')

    distance2 = ManhattanDistance2(puzzle).result
    print('\nManhattan distance (dumb way): {0}'.format(distance2))


if __name__ == '__main__':
    main()
