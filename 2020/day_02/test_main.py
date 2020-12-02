import pytest

from .main import (
    check_password_policy,
    check_updated_password_policy,
    count_passwords,
)

input_data = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]


@pytest.mark.parametrize('line, correct', (
    (input_data[0], True),
    (input_data[1], False),
    (input_data[2], True),
))
def test_check_password_policy(line, correct):
    assert check_password_policy(line) is correct


@pytest.mark.parametrize('line, correct', (
    (input_data[0], True),
    (input_data[1], False),
    (input_data[2], False),
))
def test_check_updated_password_policy(line, correct):
    assert check_updated_password_policy(line) is correct


def test_count_passwords():
    assert count_passwords(check_password_policy, input_data) == 2
    assert count_passwords(check_updated_password_policy, input_data) == 1
