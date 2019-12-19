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


if __name__ == '__main__':
    input_file = '2019/day10/input.txt'
    print(f'Input file: {input_file}')

    with open(input_file, 'r') as f:
        space_map = f.readlines()
        ms = MonitoringStation(space_map=''.join(space_map))
        coordinates, count = ms.get_best_position()
        print(
            f'Best position for monitoring station is {coordinates}'
            f' with {count} asteroids'
        )
