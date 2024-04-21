#!/usr/bin/env python3
"""
Create new leet code problem

How to use:
    ./leetcode.py https://leetcode.com/problems/rotate-array/
"""
import sys
from pathlib import Path

LEETCODE_DIR = Path('_leetcode')
TEMPLATE_FILE = LEETCODE_DIR / '__template__.py'
EXCLUDED_FILES = ['__init__.py', '__template__.py']


def create_file(url: str):
    latest_problem = max((
        i for i in LEETCODE_DIR.iterdir()
        if i.name.endswith('.py') and i.name not in EXCLUDED_FILES
    ), key=lambda x: x.name)

    number = str(int(latest_problem.name.split('_')[0]) + 1).zfill(3)
    problem_name = url.split('/')[4].replace('-', '_')
    new_file = LEETCODE_DIR / f'{number}_{problem_name}.py'

    with open(TEMPLATE_FILE, 'r') as f:
        template = f.read()
        with open(new_file, 'w') as g:
            g.write(template.replace('__PROBLEM__', url.split('description')[0]))
        print(f'File created: {new_file}')


if __name__ == '__main__':
    url = sys.argv[1]
    create_file(url)
