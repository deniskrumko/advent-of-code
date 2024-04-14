"""
https://leetcode.com/problems/majority-element
"""

from collections import (
    Counter,
    defaultdict,
)
from typing import List

import pytest


class Solution1:
    """
    Runtime 176 ms. Beats 34.85% of users with Python3
    Memory 18.02 MB. Beats 35.77% of users with Python3
    """

    def majorityElement(self, nums: List[int]) -> int:
        return sorted(Counter(nums).items(), key=lambda x: x[1])[-1][0]


class Solution2:
    """
    Runtime 166 ms. Beats 74.46% of users with Python3.
    Memory 18.03 MB. Beats 35.77% of users with Python3
    """

    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        maj = len(nums) / 2
        for n in nums:
            counts[n] += 1
            if counts[n] > maj:
                return n


class Solution3:
    """
    Runtime 169 ms. Beats 63.46% of users with Python3
    Memory 18.03 MB. Beats 35.77% of users with Python3
    """

    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) / 2
        for num, count in Counter(nums).items():
            if count > maj:
                return num


@pytest.mark.parametrize(
    "value, expected",
    (
        ([3, 2, 3], 3),  # noqa
        ([2, 2, 1, 1, 1, 2, 2], 2),  # noqa
    ),
)
def test_solution(value, expected):
    for s in [Solution1, Solution2, Solution3]:
        assert s().majorityElement(value) == expected
