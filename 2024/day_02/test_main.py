import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
    is_safe_report,
)

input_data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

@pytest.mark.parametrize('value, expected', (
    ('7 6 4 2 1', True),
    ('7 6 4 2 2', False),
    ('1 2 7 8 9', False),
    ('9 7 6 2 1', False),
    ('1 3 2 4 5', False),
    ('8 6 4 4 1', False),
    ('1 3 6 7 9', True,)
))
def test_is_safe_report(value, expected):
    assert is_safe_report(value, problem_damp=False) == expected

@pytest.mark.parametrize('value, expected', (
    ('7 6 4 2 1', True),
    ('1 2 7 8 9', False),
    ('9 7 6 2 1', False),
    ('1 3 2 4 5', True),
    ('8 6 4 4 1', True),
    ('1 3 6 7 9', True),
    ('9 1 2 3', True),
    ('1 2 3 91', True),
    ('1 2 3 91 5', True),
    ('1 2 1 3 4', True),
))
def test_is_safe_report_with_problem_damp(value, expected):
    assert is_safe_report(value, problem_damp=True) == expected


def test_function_1():
    assert function_1(input_data) == 2


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 282


def test_function_2():
    assert function_2(input_data) == 4


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 349
