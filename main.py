#!/usr/bin/env python3
"""Create new folder using template.

make new
"""

import os
import shutil

TEMPLATE_DIR = '_template'
MAKEFILE_PATH = 'Makefile'


def make_template():
    latest_year = sorted(f for f in os.listdir() if f.isdigit())[-1]
    days = sorted(f for f in os.listdir(latest_year) if f.startswith('day_'))
    latest_day = days[-1] if days else 'day_00'

    new_day_number = int(latest_day.split('_')[1]) + 1
    new_folder = f'{latest_year}/day_{str(new_day_number).zfill(2)}'

    shutil.copytree(TEMPLATE_DIR, new_folder)
    print(f'Directory created: {new_folder}')

    with open(MAKEFILE_PATH, 'r') as f:
        data = f.readlines()

    with open(MAKEFILE_PATH, 'w') as f:
        f.writelines([f'CURRENT_DAY = {new_folder}\n'] + data[1:])


if __name__ == '__main__':
    make_template()
