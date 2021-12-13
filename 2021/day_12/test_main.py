import pytest

from .main import (
    find_all_paths,
    get_count_of_all_paths,
)

input_data_1 = '''
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''.strip().split('\n')

input_data_1_paths = '''
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
'''.strip().split('\n')

input_data_1_paths_for_walk_2 = '''
start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end
'''.strip().split('\n')

input_data_2 = '''
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''.strip().split('\n')

input_data_2_paths = '''
start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end
'''.strip().split('\n')

input_data_3 = '''
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''.strip().split('\n')


@pytest.fixture
def file_input_data():
    with open('2021/day_12/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


@pytest.mark.parametrize('data, expected_paths', (
    (input_data_1, input_data_1_paths),
    (input_data_2, input_data_2_paths),
))
def test_find_all_paths(data, expected_paths):
    assert sorted(find_all_paths(data)) == sorted(expected_paths)


@pytest.mark.parametrize('data, expected_count', (
    (input_data_1, 10),
    (input_data_2, 19),
    (input_data_3, 226),
))
def test_get_count_of_all_paths(data, expected_count):
    assert get_count_of_all_paths(data) == expected_count


def test_get_count_of_all_paths_from_file(file_input_data):
    assert get_count_of_all_paths(file_input_data) == 5457


def test_find_all_paths_for_method_2():
    assert sorted(find_all_paths(input_data_1, 2)) == sorted(input_data_1_paths_for_walk_2)


@pytest.mark.parametrize('data, expected_count', (
    (input_data_1, 36),
    (input_data_2, 103),
    (input_data_3, 3509),
))
def test_get_count_of_all_paths_2(data, expected_count):
    assert get_count_of_all_paths(data, walk_method=2) == expected_count


def test_get_count_of_all_paths_2_from_file(file_input_data):
    assert get_count_of_all_paths(file_input_data, walk_method=2) == 128506
