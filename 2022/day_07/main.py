from collections import defaultdict
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'
HOMEDIR = Path('/')


def get_dir_sizes(data: str, current_dir: Path = HOMEDIR) -> dict[Path, int]:
    """Walk all directories and get sizes of each directory."""
    dir_files = defaultdict(list)

    # Populate dict with dir names and files (only their sizes) in each dir
    for command in data.splitlines():
        if command.startswith('$'):
            if 'cd' in command:
                new_dir = command.split()[-1]
                if new_dir == '..':
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir / new_dir
        elif not command.startswith('dir '):
            file_size = int(command.split()[0])
            dir_files[current_dir].append(file_size)

    # Populate dict with total size of each dir (including sub dirs)
    dir_sizes = defaultdict(int)
    for child_dir, file_sizes in dir_files.items():
        for parent_dir in set(child_dir.parents) | {child_dir}:
            dir_sizes[parent_dir] += sum(file_sizes)

    return dir_sizes


def get_small_dirs_total_size(data: str, max_size: int = 100_000) -> bool:
    """Get result for puzzle (part 1)."""
    return sum(
        size for d, size in get_dir_sizes(data).items()
        if d != HOMEDIR and size <= max_size
    )


def find_dir_to_delete(data: str, disk: int = 70_000_000, update: int = 30_000_000) -> int:
    """Get result for puzzle (part 2)."""
    dir_sizes = get_dir_sizes(data)
    free_space = dir_sizes[HOMEDIR] + update - disk
    return next(filter(lambda s: s >= free_space, sorted(dir_sizes.values())))


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {get_small_dirs_total_size(input_data)}')
        print(f'Your result (2): {find_dir_to_delete(input_data)}')
