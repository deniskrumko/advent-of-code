class WireConnector:
    """Wire connector class."""

    directions = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
    }

    def __init__(self, *routes: str):
        """Initialize class instance."""
        self.routes: str = routes
        self.map: dict = {(0, 0): set()}
        self.intersections: set = set()
        self.build_routes()

    @classmethod
    def from_file(cls, input_file: str) -> 'WireConnector':
        """Build ``WireConnector`` from file."""
        with open(input_file, 'r') as f:
            return cls(*f.readlines())

    def get_closest_intersection(self) -> int:
        """Find closest intersection between routes."""
        return min(abs(i[0]) + abs(i[1]) for i in self.intersections)

    def get_minimal_steps_to_intersection(self) -> int:
        """Get minimal steps to intersection."""
        self.results = {}

        for route in self.routes:
            for distance, cur in enumerate(self.walk_the_route(route), 1):
                if cur in self.intersections:
                    self.results.setdefault(cur, 0)
                    self.results[cur] += distance

        return min(self.results.values())

    def build_routes(self):
        """Build all routes on map."""
        for index, route in enumerate(self.routes):
            self.build_route(route, index)

    def build_route(self, route: str, index: int):
        """Build single route on map."""
        for cur in self.walk_the_route(route):
            self.map.setdefault(cur, set())
            self.map[cur].add(index)

            if len(self.map[cur]) > 1:
                self.intersections.add(cur)

    def walk_the_route(self, route: str) -> tuple:
        """Walk specified route."""
        cur = (0, 0)

        for step in route.split(','):
            direction, distance = step[0], int(step[1:])
            move = self.directions[direction]
            for _ in range(distance):
                cur = (cur[0] + move[0], cur[1] + move[1])
                yield cur


if __name__ == '__main__':
    input_file = '2019/day3/input.txt'
    print(f'Input file: {input_file}')

    runner = WireConnector.from_file(input_file)
    distance = runner.get_closest_intersection()
    print(f'Closest intersection distance: {distance}')

    steps = runner.get_minimal_steps_to_intersection()
    print(f'Min steps tp intersection: {steps}')
