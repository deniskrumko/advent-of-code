#!/usr/bin/env python
import sys

from libs import ArgsParser, registry
from solutions import *  # noqa
from tests import *  # noqa

sys.path.append("..")

if __name__ == '__main__':
    args = ArgsParser().get_arguments()

    if args.test:
        test_class = registry[args.solution]['test']
        test_class().run_tests()
    else:
        solution_class = registry[args.solution]['solution']
        solution_class().print_results()
