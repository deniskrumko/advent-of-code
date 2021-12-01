from .main import (
    count_measurement_increases,
    count_sliding_window_measurement_increases,
)

input_data = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def test_count_measurement_increases():
    assert count_measurement_increases(input_data) == 7


def test_count_sliding_window_measurement_increases():
    assert count_sliding_window_measurement_increases(input_data) == 5
