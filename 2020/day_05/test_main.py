import pytest

from .main import (
    get_max_seat_id,
    get_missing_seat_ids,
    get_seat_id,
    parse_boarding_pass,
)


@pytest.mark.parametrize('boarding_pass, row, column', (
    ('FBFBBFFRLR', 44, 5),
    ('BFFFBBFRRR', 70, 7),
    ('FFFBBBFRRR', 14, 7),
    ('BBFFBBFRLL', 102, 4),
))
def test_parse_boarding_pass(boarding_pass, row, column):
    assert parse_boarding_pass(boarding_pass) == (row, column)


@pytest.mark.parametrize('boarding_pass, seat_id', (
    ('FBFBBFFRLR', 357),
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820),
))
def test_get_seat_id(boarding_pass, seat_id):
    assert get_seat_id(boarding_pass) == seat_id


def test_get_max_seat_id():
    boarding_passes = [
        'FBFBBFFRLR',
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL',
    ]
    assert get_max_seat_id(boarding_passes) == 820


def test_2020_day_05_input():
    with open('2020/day_05/input.txt', 'r') as f:
        input_data = [line.strip() for line in f.readlines()]
        assert get_max_seat_id(input_data) == 901
        assert get_missing_seat_ids(input_data) == {661}
