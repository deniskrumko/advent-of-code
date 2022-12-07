import pytest

from .main import (
    INPUT_FILE,
    find_dir_to_delete,
    get_small_dirs_total_size,
)

input_data = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_get_small_dirs_total_size():
    assert get_small_dirs_total_size(input_data) == 95437


def test_get_small_dirs_total_size_from_file(file_input_data):
    assert get_small_dirs_total_size(file_input_data) == 1749646


def test_find_dir_to_delete():
    assert find_dir_to_delete(input_data) == 24933642


def test_find_dir_to_delete_from_file(file_input_data):
    assert find_dir_to_delete(file_input_data) == 1498966
