class Solution:
    """Base class for solutions."""

    data_file = None

    def __init__(self, data=None):
        """Initialize class instance."""
        self.data = data or self.get_data()

    def get_data(self):
        """Get data from data file."""
        assert self.data_file, 'Attribute `data_file` is not defined'

        with open(self.data_file, 'r') as f:
            return f.readlines()

    def print_results(self):
        """Run solution and show results."""
        print(f'\nClass:\t{self.__class__.__name__}')
        print(f'Result:\t{self.run()}')
