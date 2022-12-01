import math


class MonitoringStation:
    """Class for building monitoring station."""

    def __init__(self, space_map: str = None):
        """Initialize class instance."""
        self._map = [
            [i for i in line.strip()]
            for line in space_map.split('\n') if line
        ]
        self.width = len(self._map[0])
        self.height = len(self._map)
        self.history = []

    def print_map(self):
        print()

        for line in self._map:
            for value in line:
                print(value, end='')
            print()

        input('')

    def get_best_position(self) -> tuple:
        """Get best position for monitoring station."""
        max_amount = 0
        coordinates = (0, 0)

        for i in range(self.height):
            for j in range(self.width):
                if self._map[j][i] == '#':
                    amount = self.get_amount_of_visible_asteroids(i, j)
                    if amount > max_amount:
                        coordinates = (i, j)
                        max_amount = amount

        return coordinates, max_amount

    def get_amount_of_visible_asteroids(self, x, y) -> int:
        """Get amount of visible asteroids from provided coordinate."""
        counter = 0
        for i in range(self.height):
            for j in range(self.width):
                try:
                    # Access map in reverse order
                    if self._map[j][i] == '#':
                        if self.is_visible(station=(x, y), asteroid=(i, j)):
                            counter += 1
                except IndexError:
                    raise IndexError(f'j = {j}, i = {i}')

        return counter

    def is_visible(self, station: tuple, asteroid: tuple) -> bool:
        """Returns True if asteroid is visible from station."""
        if station == asteroid:
            return False

        step_x = asteroid[0] - station[0]
        step_y = asteroid[1] - station[1]
        gcd = math.gcd(step_x, step_y)
        jump = (step_x // gcd, step_y // gcd)

        current = station
        any_other_asteroids = False

        while True:
            current = (current[0] + jump[0], current[1] + jump[1])
            if current == asteroid:
                break

            # Access map in reverse order
            if self._map[current[1]][current[0]] == '#':
                any_other_asteroids = True

        return not any_other_asteroids

    def run_vaporisation(self, station: tuple):
        distance = max(self.width, self.height)
        total_counter = 0

        self._map[station[1]][station[0]] = '@'

        while True:
            found_asteroids = False
            for jump in self.get_turning_jumps(distance):
                current = station
                while True:
                    current = (current[0] + jump[0], current[1] - jump[1])
                    if current[0] < 0 or current[1] < 0:
                        break

                    try:
                        value = self._map[current[1]][current[0]]
                    except IndexError:
                        break

                    if value == '#':
                        found_asteroids = True
                        total_counter += 1
                        self._map[current[1]][current[0]] = total_counter
                        self.history.append(current)
                        break

            if not found_asteroids:
                break

        return total_counter

    @classmethod
    def get_all_moves(cls, distance):
        for i in range(distance + 1):
            for j in range(distance + 1):
                yield (i, j)

    @classmethod
    def get_turning_jumps(cls, distance):
        x = list(cls.get_all_moves(distance))
        res = set()
        for i in x:
            gcd = math.gcd(*i)
            if gcd == 0:
                continue
            res.add((i[0] // gcd, i[1] // gcd))

        def myfunc(coord):
            if coord == (1, 0):
                return 0
            if coord == (0, 1):
                return 90
            return math.degrees(math.atan(coord[1] / coord[0]))

        p1 = list(reversed(sorted(list(res), key=myfunc)))
        p2 = [(i, -j) for i, j in p1]
        p2[0], p2[-1] = p2[-1], p2[0]
        p3 = [(-i, -j) for i, j in p1]
        p4 = [(-j, i) for i, j in p1]
        result = p1 + p2[1:] + p3[1:] + p4[1:-1]
        return result


if __name__ == '__main__':
    input_file = '2019/day10/input.txt'
    print(f'Input file: {input_file}')

    with open(input_file, 'r') as f:
        space_map = f.readlines()
        ms = MonitoringStation(space_map=''.join(space_map))
        coordinates, count = ms.get_best_position()
        print(
            f'Best position for monitoring station is {coordinates}'
            f' with {count} asteroids',
        )

        ms.run_vaporisation(station=coordinates)
        asteroid_200 = ms.history[199]
        print(f'Asteroid #200 that was vaporised is {asteroid_200}')

        code = asteroid_200[0] * 100 + asteroid_200[1]
        print(f'Secret code: {code}')  # 1707
