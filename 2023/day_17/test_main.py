import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data_1 = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""".strip('\n')

input_data_2 = """
113
919
911
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

@pytest.mark.parametrize('value, expected', (
    (input_data_1, 102),
    (input_data_2, 4),
))
def test_function_1(value, expected):
    assert function_1(value) == expected


@pytest.mark.skip('Not ready')
def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data)


@pytest.mark.skip('Not ready')
def test_function_2():
    assert function_2(input_data_1)


@pytest.mark.skip('Not ready')
def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data)
