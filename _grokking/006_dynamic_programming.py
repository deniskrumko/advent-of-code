
import numpy as np
import pandas as pd
import pytest


def solve_thief_problem(values: dict, max_bag_size: int) -> tuple[int, list[str]]:
    """Help thief to steal maximum value of items with limited bag size.

    Dynamic programming splits original problem to smaller problems and find local maximum at each
    step. On each step we write cell (df[i][j]) with maximum among following choices:

        1. Previous maximum for this amount of space -> df[i - 1][j]
        2. Current object price + price of free space (already calculated) -> df[i - 1][j - obj_w]
    """
    prices_dict = {k: v[0] for k, v in values.items()}
    weights_dict = {k: v[1] for k, v in values.items()}

    # This is not the best way to find step size!
    step_size = 1
    min_weight = min(weights_dict.values())
    if min_weight < step_size:
        step_size = min_weight

    columns = max_bag_size / step_size
    if int(columns) != columns:
        raise ValueError(f'Max bag size can not be divided by step size ({step_size})')

    df = pd.DataFrame(
        index=values,
        columns=np.arange(step_size, max_bag_size + step_size, step_size),
    )
    for i, obj in enumerate(df.index):
        obj_w = weights_dict[obj]
        obj_p = prices_dict[obj]

        for j in df.columns:
            # Estimate free space in bag after we put current object in it
            free_w = j - obj_w

            # Collecting items to compare
            to_compare = []

            # If previous max exists
            if i > 0:
                to_compare.append(df.iloc[i - 1][j])

            # If free space fits current object and more
            if free_w > 0 and i > 0:
                free_p, obj_list = df.iloc[i - 1][free_w]
                to_compare.append((obj_p + free_p, obj_list + [obj]))

            # If free space fits only current object or there is nothing to compare with
            if not to_compare or free_w == 0:
                to_compare.append((obj_p, [obj]) if free_w >= 0 else (0, []))

            # Set local maximum
            df.iloc[i][j] = max(to_compare, key=lambda x: x[0])

    price, objects = df.iloc[-1][max_bag_size]
    return price, sorted(objects)


@pytest.mark.parametrize('value, max_bag_size, expected', (
    (
        # item name: (item price in $, item weight in kg)
        {
            'guitar': (1500, 1),
            'recorder': (3000, 4),
            'notebook': (2000, 3),
        },
        4,
        (3500, ['guitar', 'notebook']),
    ),
    (
        {
            'guitar': (1500, 1),
            'notebook': (2000, 3),
            'recorder': (3000, 4),
            'iphone': (2000, 1),
        },
        4,
        (4000, ['iphone', 'notebook']),
    ),
    (
        {
            'guitar': (1500, 1),
            'notebook': (2000, 3),
            'recorder': (3000, 4),
            'iphone': (2000, 1),
            'mp3': (1000, 1),
        },
        4,
        (4500, ['guitar', 'iphone', 'mp3']),
    ),
    (
        {
            'guitar': (1500, 1),
            'notebook': (2000, 3),
            'recorder': (3000, 4),
            'iphone': (2000, 1),
            'necklace': (3000, 0.5),
        },
        4,
        (6500, ['guitar', 'iphone', 'necklace']),
    ),
    (
        {
            'guitar': (1500, 1),
            'notebook': (2000, 3),
            'recorder': (3000, 4),
            'iphone': (2000, 1),
            'necklace': (3000, 0.5),
        },
        3.5,
        (6500, ['guitar', 'iphone', 'necklace']),
    ),
    (
        {
            'guitar': (1500, 1),
            'notebook': (2000, 3),
            'recorder': (3000, 4),
            'iphone': (2000, 1),
            'necklace': (3000, 0.5),
        },
        0.5,
        (3000, ['necklace']),
    ),
    (
        {
            'notebook': (2000, 3),
            'recorder': (3000, 4),
        },
        1,
        (0, []),
    ),
))
def test_solve_thief_problem(value, max_bag_size, expected):
    assert solve_thief_problem(value, max_bag_size=max_bag_size) == expected


def solve_tourist_problem(values: dict, max_days: int) -> tuple[int, list[str]]:
    """Help to plan best trip for tourist.

    It's just the same as thief problem :))
    """
    return solve_thief_problem(
        values=values,
        max_bag_size=max_days,
    )


@pytest.mark.parametrize('value, max_days, expected', (
    (
        {
            # place name: (rating in stars, time to spend)
            'вестминстер': (7, 0.5),
            'театр': (6, 0.5),
            'галерея': (9, 1),
            'музей': (9, 2),
            'собор': (8, 0.5),
        },
        2,
        (24, ['вестминстер', 'галерея', 'собор']),
    ),
))
def test_solve_tourist_problem(value, max_days, expected):
    assert solve_tourist_problem(value, max_days=max_days) == expected


def get_longest_substring(string_a: str, string_b: str) -> str:
    """Get longest substring - dynamic programming way.

    Estimated complexity: O(n*m)

    Possible optimizations:
        1. Save max value and position during the cycle
        2. Don't use dataframes
    """
    df = pd.DataFrame(
        index=range(len(string_a)),
        columns=range(len(string_b)),
        dtype=np.integer,
    )
    for i, a_char in enumerate(string_a):
        for j, b_char in enumerate(string_b):
            if a_char == b_char and i > 0 and j > 0:
                df.iloc[i][j] = df.iloc[i - 1][j - 1] + 1
            else:
                df.iloc[i][j] = 1 if a_char == b_char else 0

    length = int(df.values.max())
    index = int(df.stack().idxmax()[0]) + 1
    return string_a[index - length:index]


def get_longest_substring_different_way(string_a: str, string_b: str) -> str:
    """Get longest substring - my way :)

    Estimated complexity: O(n^2 * m), where n - length of smallest string
    """
    min_str, max_str = (
        (string_a, string_b)
        if len(string_a) < len(string_b)
        else (string_b, string_a)
    )

    long_sub = ''
    for i in range(len(min_str) + 1):  # O(n)
        for j in range(i + 1, len(min_str) + 1):  # O(n)
            subs = min_str[i:j]
            if subs not in max_str:  # O(m)
                break

            if len(subs) > len(long_sub):
                long_sub = subs

    return long_sub


@pytest.mark.parametrize('value, expected', (
    (['fish', 'hish'], 'ish'),
    (['hish', 'vista'], 'is'),
    (['dog', 'cat'], ''),
    (['My name is Denis', 'Denis is me!'], 'Denis'),
    (['My name is Denis', 'Denis is my name!'], 'y name'),
))
def test_get_longest_substring(value, expected):
    assert get_longest_substring(*value) == expected
    assert get_longest_substring_different_way(*value) == expected


def levenshtein_distance(str_a, str_b) -> int:
    # Memory optimization -> smallers string is stored in memory
    if len(str_a) > len(str_b):
        str_a, str_b = str_b, str_a  # str_a should be smaller than str_b

    # Algorithm requires only current and previous lines in memory
    len_a, len_b = len(str_a), len(str_b)
    cur_line = range(len_a + 1)
    for i in range(1, len_b + 1):
        prev_line, cur_line = cur_line, [i] + [None] * len_a
        for j in range(1, len_a + 1):
            a, b = str_a[j - 1], str_b[i - 1]
            cur_line[j] = min(cur_line[j - 1] + 1, prev_line[j] + 1, prev_line[j - 1] + int(a != b))

    return cur_line[-1]


@pytest.mark.parametrize('value, expected', (
    (['лабрадор', 'гибралтар'], 5),
    (['котик', 'скотина'], 3),
    (['австрия', 'австралия'], 2),
    (['биба', 'боба'], 1),
))
def test_levenshtein_distance(value, expected):
    assert levenshtein_distance(*value) == expected
