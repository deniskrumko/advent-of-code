import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
    get_arrangements,
    unfold_line,
)

input_data = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

@pytest.mark.parametrize('i, expected', (
    (0, 1),
    (1, 4),
    (2, 1),
    (3, 1),
    (4, 4),
    (5, 10),
))
def test_get_arrangements(i, expected):
    assert len(get_arrangements(input_data.splitlines()[i])) == expected


@pytest.mark.parametrize('line, expected', (
    ('.# 1', '.#?.#?.#?.#?.# 1,1,1,1,1'),
    ('???.### 1,1,3', '???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3'),
))
def test_unfold_line(line, expected):
    assert unfold_line(line) == expected


def test_function_1():
    assert function_1(input_data) == 21


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 7191


@pytest.mark.skip('Not ready')
def test_function_2():
    assert function_2(input_data) == 525152


@pytest.mark.skip('Not ready')
def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data)
