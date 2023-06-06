import math

import pytest

sample_1 = [i for i in range(1, 11)]
sample_2 = [i for i in range(100, 0, -1)]
sample_3 = [123, 12, 1, 1, 1, 0, -300, 125, 123]
all_samples = [sample_1, sample_2, sample_3]


def rec_sum(array):
    """Recursive sum of array elements."""
    return 0 if len(array) == 0 else array[0] + rec_sum(array[1:])


def rec_len(array):
    """Recursive length of array."""
    return 0 if not array else 1 + rec_len(array[1:])


def rec_max(array, found_max=None):
    """Recursive max element if array."""
    if not array:
        return found_max

    if found_max is None:
        found_max = array[0]

    if array[0] > found_max:
        return rec_max(array[1:], found_max=array[0])
    else:
        return rec_max(array[1:], found_max=found_max)


def rec_max_2(array):
    """Recursive max element if array (more optimal)."""
    if len(array) == 1:
        return array[0]

    left, right = array[0], rec_max_2(array[1:])
    return left if left > right else right


def rec_factorial(value):
    """Recursive factorial."""
    return 1 if value in (0, 1) else value * rec_factorial(value - 1)


def rec_fib(n):
    """Recursive N Fibonacci number."""
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n < 1:
        return None

    return rec_fib(n - 1) + rec_fib(n - 2)


def rec_gcd_simplified(a, b):
    """Recursive Euclidean algorithm (GCD) - simplified version for positive numbers only."""
    return a if a == b else rec_gcd_simplified(a if a < b else b, abs(a - b))


def rec_gcd_full(a, b):
    """Recursive Euclidean algorithm (GCD) - full version."""
    return abs(a + b) if (a == 0 or b == 0) else rec_gcd_simplified(abs(a), abs(b))


# TESTS
# =============================================================================================

def test_rec_sum():
    for sample in all_samples:
        assert rec_sum(sample) == sum(sample)


def test_rec_sum_empty():
    rec_sum([])


def test_rec_len():
    for sample in all_samples:
        assert rec_len(sample) == len(sample)


def test_rec_max():
    for sample in all_samples:
        assert rec_max(sample) == rec_max_2(sample) == max(sample)


def test_rec_factorial():
    for i in range(0, 11):
        assert rec_factorial(i) == math.factorial(i)


@pytest.mark.parametrize('n, expected', [
    (-1, None),
    (0, None),
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
    (9, 21),
    (10, 34),
])
def test_rec_fib(n, expected):
    assert rec_fib(n) == expected


@pytest.mark.parametrize('a, b', (
    (1680, 640),
    (1680, 641),
    (1, 2),
    (3, 21),
    (-3, 1),
    (-3, -7),
    (4, 0),
    (-4, 0),
    (1, 1),
))
def test_rec_gcd(a, b):
    expected = math.gcd(a, b)
    if a > 0 and b > 0:
        assert rec_gcd_simplified(a, b) == expected

    assert rec_gcd_full(a, b) == expected
