from functools import lru_cache
from itertools import product

import pytest


@lru_cache(maxsize=8)
def generate_parentheses(n) -> set[str]:
    if n == 1:
        return {'()'}

    result = set()
    for i in range(1, n):
        a, b = generate_parentheses(i), generate_parentheses(n - i)
        if i == 1:
            result.update(f'({var})' for var in b)
        result.update(''.join(var) for var in product(a, b))

    return result


@pytest.mark.parametrize('value, expected', (
    (1, ['()']),
    (2, ['()()', '(())']),
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
))
def test_generate_parentheses(value, expected):
    assert sorted(generate_parentheses(value)) == sorted(expected)


if __name__ == '__main__':
    import time
    time_start = time.time()
    variations = generate_parentheses(n=8)
    time_end = time.time()
    for val in variations:
        print(val)
    print(f'Operation done in {time_end - time_start:.6f} seconds')
