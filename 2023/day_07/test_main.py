import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
    get_hand,
    joker_pretend,
)

input_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 6440


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 250898830


def test_function_2():
    assert function_2(input_data) == 5905


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 252127335

# TEST HELPERS


@pytest.mark.parametrize('cards, expected', (
    ('AAAAA', 0),
    ('AA8AA', 1),
    ('23332', 2),
    ('TTT98', 3),
    ('23432', 4),
    ('A23A4', 5),
    ('23456', 6),
))
def test_get_hand(cards, expected):
    assert get_hand(cards) == expected


@pytest.mark.parametrize('cards, pretended, hand_type', (
    ('QQQJQ', 'QQQQQ', 0),
    ('JJJJJ', 'AAAAA', 0),
    ('JJJJK', 'KKKKK', 0),
    ('KJJJK', 'KKKKK', 0),
    ('T55J5', 'T5555', 1),
    ('KTJJT', 'KTTTT', 1),
    ('QQQJA', 'QQQQA', 1),
    ('QJJQ2', 'QQQQ2', 1),
    ('337J7', '33777', 2),
    ('2J245', '22245', 3),
    ('QJKK3', 'QKKK3', 3),
    ('QQKK3', 'QQKK3', 4),
    ('JJ234', '44234', 3),
    ('J2345', '52345', 5),
    ('2345J', '23455', 5),
    ('J2A45', 'A2A45', 5),
    ('JK5KK', 'KK5KK', 1),
))
def test_joker_pretend(cards, pretended, hand_type):
    assert joker_pretend(cards) == pretended
    assert get_hand(pretended) == hand_type
