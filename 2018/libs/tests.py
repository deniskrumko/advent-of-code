from .registry import registry


class TestCase:
    """Base test case class."""

    @property
    def solution_class(self):
        """Get class of solution."""
        return registry[self.key]['solution']

    def run_tests(self):
        """Run tests and show message."""
        self.run()
        print('Tests successfully passed!')
