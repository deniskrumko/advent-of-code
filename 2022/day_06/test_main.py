import pytest

from .main import (
    INPUT_FILE,
    get_first_unique_packet,
)


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read().strip()


# TESTS

@pytest.mark.parametrize('value, window, expected', (
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4, 7),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 4, 5),
    ('nppdvjthqldpwncqszvftbrmjlhg', 4, 6),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4, 10),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4, 11),
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14, 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 14, 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 14, 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14, 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14, 26),
))
def test_get_first_unique_packet(value, window, expected):
    assert get_first_unique_packet(value, window) == expected


def test_get_first_unique_packet_from_file(file_input_data):
    assert get_first_unique_packet(file_input_data, 4) == 1544
    assert get_first_unique_packet(file_input_data, 14) == 2145
