import pytest

from .main import expense_report

input_data = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


@pytest.mark.parametrize('numbers_amount, expected', (
    (2, 514579),
    (3, 241861950),
))
def test_expense_report(numbers_amount, expected):
    assert expense_report(input_data, numbers_amount) == expected
