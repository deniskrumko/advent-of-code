import pytest

from .main import (
    INPUT_FILE,
    simulate_rope_bridge,
)

input_data = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip('\n')

input_data_2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

@pytest.mark.parametrize('value, knots, expected', (
    (input_data, 2, 13),
    (input_data, 10, 1),
    (input_data_2, 10, 36),
))
def test_simulate_rope_bridge(value, knots, expected):
    assert simulate_rope_bridge(value, knots) == expected


@pytest.mark.parametrize('knots, expected', (
    (2, 6197),
    (10, 2562),
))
def test_simulate_rope_bridge_from_file(file_input_data, knots, expected):
    assert simulate_rope_bridge(file_input_data, knots) == expected
