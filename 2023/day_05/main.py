from dataclasses import dataclass
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


class MapLine:
    """Class for single map instruction (dst-src-range)."""

    def __init__(self, line: str):
        """Initialize class instance."""
        self.dst, src, length = [int(v) for v in line.split()]
        self.start, self.end = src, src + length

    def includes(self, value: int):
        """Check if map line includes value in current range."""
        return self.start <= value < self.end

    def transition(self, value: int):
        """Make src -> dst transition for value."""
        return (value - self.start) + self.dst


@dataclass
class Range:
    """Class for storing ranges like [A,B)."""

    left: int
    right: int

    def walk(self, maps):
        """Walk current range with given maps.

        Walking is the same as applying map lines for single value, but now we need to to it
        for both left/right range borders.
        """
        for im, map_ in enumerate(maps):
            for map_line in map_:
                if self.is_left_border_in(map_line):
                    if self.is_right_border_in(map_line):
                        # If both borders of ranges fit map line -> transition to next map
                        self.transition(map_line)
                        break
                    else:
                        # If only left border fits map line -> we need to split range and try again
                        range_a, range_b = self.split_range(map_line)
                        min_a = range_a.walk(maps[im:])
                        min_b = range_b.walk(maps[im:])
                        return min(min_a, min_b)

        return self.left

    def transition(self, map_line):
        """Apply map line transition to both left/right borders."""
        self.left = map_line.transition(self.left)
        self.right = map_line.transition(self.right)

    def is_left_border_in(self, map_line: MapLine) -> bool:
        """Check if left border is in map line."""
        return map_line.start <= self.left < map_line.end

    def is_right_border_in(self, map_line: MapLine) -> bool:
        """Check if right border is in map line."""
        return map_line.start <= self.right <= map_line.end

    def split_range(self, map_line: MapLine) -> tuple['Range', 'Range']:
        """Split current range to two new ranges using map line."""
        return (
            Range(left=self.left, right=map_line.end),
            Range(left=map_line.end, right=self.right),
        )


def parse_data(data: str) -> tuple[list[int], list[list]]:
    """Parse string data to seeds and maps."""
    seeds, sections = None, []
    for section in data.split('\n\n'):
        if seeds is None:
            seeds = [int(v) for v in section.split(':')[1].split()]
        else:
            section_map = [MapLine(line) for line in section.splitlines()[1:]]
            sections.append(section_map)

    return seeds, sections


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    seeds, maps = parse_data(data)
    min_location = float('+inf')
    for seed in seeds:
        for map_ in maps:
            for map_line in map_:
                if map_line.includes(seed):
                    seed = map_line.transition(seed)
                    break

        min_location = min(seed, min_location)
    return min_location


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    seeds, maps = parse_data(data)
    min_location = float('+inf')
    for i in range(0, len(seeds), 2):
        walk_result = Range(left=seeds[i], right=seeds[i] + seeds[i + 1]).walk(maps)
        min_location = min(walk_result, min_location)
    return min_location


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
