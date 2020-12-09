import pytest

from .main import (
    build_bags_graph,
    get_bag_childs_amount,
    get_bag_parents_amount,
)

input_data = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

input_data_2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""


def test_build_bags_graph():
    bags = build_bags_graph(input_data)
    assert len(bags) == 9


def test_get_ancestors():
    bags = build_bags_graph(input_data)
    ancestors = bags['shiny gold'].get_ancestors()
    assert sorted(x.color for x in ancestors) == [
        'bright white',
        'dark orange',
        'light red',
        'muted yellow',
    ]


def test_get_bag_parents_amount():
    assert get_bag_parents_amount(input_data) == 4


@pytest.mark.parametrize('value, expected', (
    (input_data, 32),
    (input_data_2, 126),
))
def test_get_bag_childs_amount(value, expected):
    assert get_bag_childs_amount(value) == expected


def test_2020_day_07_input():
    with open('2020/day_07/input.txt', 'r') as f:
        input_data = f.read()
        assert get_bag_parents_amount(input_data) == 265
        assert get_bag_childs_amount(input_data) == 14177
