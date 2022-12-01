from collections import Counter

import pytest

from .main import (
    apply_polymerization_by_steps,
    build_template_from_str,
    get_elements_count,
    parse_data,
)

input_data = '''
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''.strip().split('\n')


@pytest.fixture
def file_input_data():
    with open('2021/day_14/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


# def test_find_most_and_least_common_score(file_input_data):
#     assert find_most_and_least_common_score(input_data) == 1588
#     assert find_most_and_least_common_score(file_input_data) == 2194


@pytest.mark.parametrize('expected, steps', (
    ('NCNBCHB', 1),
    ('NBCCNBBBCBHCB', 2),
    ('NBBBCNCCNBBNBNBBCHBHHBCHB', 3),
    ('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB', 4),
))
def test_apply_polymerization_by_steps(expected, steps):
    template, rules = parse_data(input_data)
    apply_polymerization_by_steps(template, rules, steps)

    expected_template = build_template_from_str(expected)
    assert template == expected_template


# @pytest.mark.parametrize('expected, steps', (
#     # ('NCNBCHB', 1),
#     ('NBCCNBBBCBHCB', 2),
#     # ('NBBBCNCCNBBNBNBBCHBHHBCHB', 3),
#     # ('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB', 4),
# ))
# def test_get_elements_count(expected, steps):
#     template, rules = parse_data(input_data)
#     apply_polymerization_by_steps(template, rules, steps)

#     elements = get_elements_count(template)
#     for element, expected_count in Counter(expected).items():
#         assert elements[element] == expected_count, (
#             f'Incorrect count for step {steps} ({expected}).\n'
#             f'Got {element}={elements[element]} but expected {element}={expected_count}!'
#         )


# def test_function_1_from_file(file_input_data):
#     assert function(file_input_data)


# def test_function_2():
#     assert function(input_data)


# def test_function_2_from_file(file_input_data):
#     assert function(file_input_data)
