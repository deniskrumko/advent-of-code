from collections import (
    Counter,
    defaultdict,
)


def build_tree(data: list) -> dict:
    """Build tree of connecting caves."""
    tree = defaultdict(set)
    for line in data:
        a, b = line.split('-')
        tree[a].add(b)
        tree[b].add(a)

    return tree


def walk_tree_1(tree, walked_path: list, total_paths: list, current_point: str) -> None:
    """Walk tree (method 1).

    Allows to visit small caves only once and large caves - any number of times.
    """
    for direction in tree[current_point]:
        if direction == 'start':
            continue

        if direction == 'end':
            total_paths.append(walked_path + [current_point, direction])
            continue

        if direction.islower() and direction in walked_path:
            continue

        walk_tree_1(tree, walked_path + [current_point], total_paths, direction)


def walk_tree_2(tree, walked_path: list, total_paths: list, current_point: str) -> None:
    """Walk tree (method 2).

    Allows to visit small caves only once (expect only one small cave can be visited twice)
    and large caves - any number of times.
    """
    walked_path = walked_path + [current_point]

    for direction in tree[current_point]:
        if direction == 'start':
            continue

        if direction == 'end':
            total_paths.append(walked_path + [direction])
            continue

        if direction.islower() and direction in walked_path:
            if any(
                cave.islower() and times_visited == 2
                for cave, times_visited in Counter(walked_path).items()
            ):
                continue

        walk_tree_2(tree, walked_path, total_paths, direction)


def find_all_paths(data: list, walk_method: int = 1) -> list[str]:
    """Find all possible paths from start to end."""
    tree = build_tree(data)
    total_paths = []

    walk_func = {1: walk_tree_1, 2: walk_tree_2}[walk_method]
    walk_func(tree, walked_path=[], total_paths=total_paths, current_point='start')
    return [','.join(path) for path in total_paths]


def get_count_of_all_paths(data: list, walk_method: int = 1) -> int:
    """Get amount of all possible paths for current walk method."""
    return len(find_all_paths(data, walk_method))


if __name__ == '__main__':
    with open('2021/day_12/input.txt', 'r') as f:
        input_data = [line.strip() for line in f.readlines()]
        print(f'Your result (1): {get_count_of_all_paths(input_data, 1)}')
        print(f'Your result (2): {get_count_of_all_paths(input_data, 2)}')
