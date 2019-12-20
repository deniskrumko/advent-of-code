import pytest

from .main import MonitoringStation
from .maps import (
    map_1,
    map_2,
    map_3,
    map_4,
    map_5,
)


@pytest.mark.parametrize('space_map,x,y,count', (
    (map_1, 3, 4, 8),
    (map_2, 5, 8, 33),
    (map_3, 1, 2, 35),
    (map_4, 6, 3, 41),
    (map_5, 11, 13, 210),
))
def test_get_amount_of_visible_asteroids(space_map, x, y, count):
    """Test `get_amount_of_visible_asteroids`."""
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
    """Test `get_best_position.`"""
    ms = MonitoringStation(space_map.strip())
    coordinates, asteroids = ms.get_best_position()
    assert coordinates == (x, y)
    assert asteroids == expected_count


@pytest.mark.parametrize('distance,expected', (
    (1, 8 * 1),
    (2, 8 * 2),
    (3, 8 * 4),
    (4, 8 * 6),
    (5, 8 * 10),
))
def test_get_turning_jumps(distance, expected):
    """Test `get_turning_jumps`."""
    jumps = list(MonitoringStation.get_turning_jumps(distance))
    assert len(jumps) == expected


def test_run_vaporisation():
    """Test `run_vaporisation`."""
    ms = MonitoringStation(map_1.strip())
    result = ms.run_vaporisation(station=(3, 4))
    assert result == 9


@pytest.mark.parametrize('order,coordinates', (
    (1, (11, 12)),
    (2, (12, 1)),
    (3, (12, 2)),
    (10, (12, 8)),
    (20, (16, 0)),
    (50, (16, 9)),
    (100, (10, 16)),
    (199, (9, 6)),
    (200, (8, 2)),
    (201, (10, 9)),
    (299, (11, 1)),
))
def test_map_5_vaporisation(order, coordinates):
    """Test vaporisation order on map #5."""
    ms = MonitoringStation(map_5.strip())
    ms.run_vaporisation(station=(11, 13))
    assert ms.history[order - 1] == coordinates
