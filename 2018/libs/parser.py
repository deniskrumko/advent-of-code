from argparse import ArgumentParser


class ArgsParser():
    """Parse arguments"""

    def __init__(self):
        """Initialize class instance."""
        self.parser = ArgumentParser(
            epilog='2018 (c) Denis Krumko',
        )
        self.parser.add_argument(
            'solution',
            type=str,
            metavar='<day>.<part>',
            help='Number of day and part (1.1 for example)',
        )
        self.parser.add_argument(
            '-t',
            '--test',
            action='store_true',
            help='Run tests',
        )

    def get_arguments(self):
        """Get arguments."""
        return self.parser.parse_args()
