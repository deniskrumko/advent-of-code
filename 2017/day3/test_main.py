from .main import (
    AdjacentSquares,
    ManhattanDistance,
)


def test_manhattan_distance():
    distance_tests = {
        1: 0,
        12: 3,
        23: 2,
        1024: 31,
    }

    for test, result in distance_tests.items():
        assert ManhattanDistance(test).result == result


def test_adjacent_squares():
    adjacent_squares_tests = {
        4: 5,
        5: 10,
        10: 11,
        11: 23,
        23: 25,
        25: 26,
        747: 806,
    }

    for test, result in adjacent_squares_tests.items():
        assert AdjacentSquares(test).result == result
