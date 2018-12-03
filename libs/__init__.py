from .parser import ArgsParser
from .registry import register, registry
from .solution import Solution
from .tests import TestCase

__all__ = (
    'ArgsParser',
    'Solution',
    'TestCase',
    'register',
    'registry',
)
