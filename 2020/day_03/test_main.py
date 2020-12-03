from .main import (
    check_all_scopes,
    traverse_map,
)

input_data = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".split()


def test_traverse_map():
    assert traverse_map(input_data) == 7


def test_check_all_scopes():
    assert check_all_scopes(input_data) == 336
