from itertools import zip_longest


def polynom_sum(input: str) -> tuple:
    lines = input.splitlines()
    a, b = map(
        lambda x: reversed([int(val) for val in x.split()]),
        (lines[1], lines[3]),
    )
    res = list(map(sum, zip_longest(a, b, fillvalue=0)))
    return (
        len(res) - 1,  # polynom size
        ' '.join(str(v) for v in reversed(res)),  # polynom values
    )


def test_polynom_sum():
    val = '''
    3
    1 2 3 4
    2
    1 0 0
    '''.strip()
    assert polynom_sum(val) == (3, '1 3 3 4')
