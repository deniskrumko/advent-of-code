#!/usr/bin/env python3
"""Create new folder using template.

RUN: ./template.py
"""

import os
import shutil

TEMPLATE_DIR = '_template'


def main():
    latest_year = sorted(f for f in os.listdir() if f.isdigit())[-1]
    days = sorted(f for f in os.listdir(latest_year) if f.startswith('day_'))
    latest_day = days[-1] if days else 'day_00'

    new_day_number = int(latest_day.split('_')[1]) + 1
    new_folder = f'{latest_year}/day_{str(new_day_number).zfill(2)}'

    shutil.copytree(TEMPLATE_DIR, new_folder)
    print(f'Directory created: {new_folder}')


if __name__ == '__main__':
    main()
