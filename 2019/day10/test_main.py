import pytest
from .main import MonitoringStation

map_1 = """
.#..#
.....
#####
....#
...##
"""

map_2 = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""

map_3 = """
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
"""

map_4 = """
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
"""

map_5 = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""


@pytest.mark.parametrize('space_map,x,y,count', (
    (map_1, 3, 4, 8),
    (map_2, 5, 8, 33),
    (map_3, 1, 2, 35),
    (map_4, 6, 3, 41),
    (map_5, 11, 13, 210),
))
def test_get_amount_of_visible_asteroids(space_map, x, y, count):
    ms = MonitoringStation(space_map.strip())
    assert ms.get_amount_of_visible_asteroids(x, y) == count


@pytest.mark.parametrize('space_map,x,y,expected_count', (
    (map_1, 3, 4, 8),
    (map_2, 5, 8, 33),
    (map_3, 1, 2, 35),
    (map_4, 6, 3, 41),
    (map_5, 11, 13, 210),
))
def test_get_best_position(space_map, x, y, expected_count):
    ms = MonitoringStation(space_map.strip())
    coordinates, asteroids = ms.get_best_position()
    assert coordinates == (x, y)
    assert asteroids == expected_count
