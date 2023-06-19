import os
from pathlib import Path


def new_problem():
    cur_dir = Path('_grokking')
    name = input('Problem name: ')
    slug = '_'.join(w.lower() for w in name.split())

    last_task = 0
    for filename in os.listdir(cur_dir):
        number = filename.split('_')[0]
        if number.isdigit() and int(number) > last_task:
            last_task = int(number)

    new_task_name = f'{str(last_task + 1).zfill(3)}_{slug}.py'
    filepath = cur_dir / new_task_name
    filepath.touch()
    print(filepath)


if __name__ == '__main__':
    new_problem()
