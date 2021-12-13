import pytest

from .main import (
    count_syntax_checker_points_for_corrupted,
    count_syntax_checker_points_for_incomplete,
    get_score_for_incomplete_line,
    parse_line,
)

input_data = '''
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''.strip().split('\n')


@pytest.fixture
def file_input_data():
    with open('2021/day_10/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


@pytest.mark.parametrize('value, expected', (
    ('([])', True),
    ('{()()()}', True),
    ('<([{}])>', True),
    ('[<>({}){}[([])<>]]', True),
    ('(((((((((())))))))))', True),
    ('(]', False),
    ('{()()()>', False),
    ('(((()))}', False),
    ('<([]){()}[{}])', False),
    ('[({(<(())[]>[[{[]{<()<>>', None),
    ('{([(<{}[<>[]}>{[]{[(<()>', False),
))
def test_parse_line(value, expected):
    assert parse_line(value)[0] is expected, f'Wrong for {value}'


def test_count_syntax_checker_points_for_corrupted(file_input_data):
    assert count_syntax_checker_points_for_corrupted(input_data) == 26397
    assert count_syntax_checker_points_for_corrupted(file_input_data) == 469755


@pytest.mark.parametrize('line, score, completion_line', (
    (input_data[0], 288957, '}}]])})]'),
    (input_data[1], 5566, ')}>]})'),
    (input_data[3], 1480781, '}}>}>))))'),
))
def test_get_score_for_incomplete_line(line, score, completion_line):
    assert get_score_for_incomplete_line(line) == (score, completion_line)


def test_count_syntax_checker_points_for_incomplete(file_input_data):
    assert count_syntax_checker_points_for_incomplete(input_data) == 288957
    assert count_syntax_checker_points_for_incomplete(file_input_data) == 2762335572
