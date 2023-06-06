import pytest

sample = [i for i in range(100)]
sample_2 = [3, 19, 24, 26, 99, 1020, 9999, 1000001]


def my_binary_search(array, value, low=None, high=None):
    if low is None:
        low, high = 0, len(array) - 1

    mid_pos = (low + high) // 2
    mid_val = array[mid_pos]

    if value == mid_val:
        return mid_pos
    elif high == low:
        return None
    elif value > mid_val:
        return my_binary_search(array, value, low=mid_pos + 1, high=high)
    elif value < mid_val:
        return my_binary_search(array, value, low=low, high=mid_pos)


@pytest.mark.parametrize('value, position', (
    (0, 0),
    (99, 99),
    (50, 50),
    (51, 51),
    (-1, None),
    (100, None),
))
def test_my_binary_search_sample_1(value, position):
    if position is not None:
        assert sample[position] == value
    assert my_binary_search(sample, value) == position


def test_my_binary_search_sample_2():
    for position, value in enumerate(sample_2):
        assert my_binary_search(sample_2, value) == position

    assert my_binary_search(sample_2, 777) is None
    assert my_binary_search(sample_2, -300) is None
