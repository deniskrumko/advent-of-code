import math
from pathlib import Path
from typing import (
    Iterator,
    Optional,
)

INPUT_FILE = Path(__file__).parent / 'input.txt'
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_visible(
    i: int,
    j: int,
    direction: tuple,
    tree_map: list,
    tree_height: Optional[int] = None,
    tree_count: int = 0,
):
    """Find visible trees in specific direction."""
    if tree_height is None:
        tree_height = tree_map[i][j]

    i, j = i + direction[0], j + direction[1]
    if i < 0 or j < 0 or i > len(tree_map) - 1 or j > len(tree_map[0]) - 1:
        return True, tree_count

    tree_count += 1
    new_tree_height = tree_map[i][j]
    if int(new_tree_height) >= int(tree_height):
        return False, tree_count

    return find_visible(i, j, direction, tree_map, tree_height, tree_count)


def tree_is_visible(i: int, j: int, tree_map: list) -> bool:
    """Check if tree is visible in any direction."""
    return any(find_visible(i, j, d, tree_map)[0] for d in DIRECTIONS)


def scenic_score(i: int, j: int, tree_map: list) -> list:
    """Count scenic score for tre.."""
    return math.prod(find_visible(i, j, d, tree_map)[1] for d in DIRECTIONS)


def walk_map(tree_map: list) -> Iterator[tuple]:
    """Walk tree map."""
    for i in range(len(tree_map)):
        for j in range(len(tree_map[0])):
            yield i, j


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    tree_map = data.splitlines()
    return sum(tree_is_visible(i, j, tree_map) for i, j in walk_map(tree_map))


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    tree_map = data.splitlines()
    return max(scenic_score(i, j, tree_map) for i, j in walk_map(tree_map))


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
