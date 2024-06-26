"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
"""

from collections import Counter
from typing import List

import pytest


class Solution1:
    """First dumb solution.

    Complexity: O(2n) -> O(n)
    Memory: O(2n) -> O(n)
    Runtime 50 ms. Beats 68.37% of users with Python3 👍.
    Memory 16.66 MB. Beats 25.10% of users with Python3 👎.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for val, number in Counter(nums).items():
            for _ in range(min(2, number)):
                nums[i] = val
                i += 1
        return i


class Solution2:
    """In-place solution. Better algoritmically.

    Complexity: O(n)
    Memory: O(2n) -> O(n)
    Runtime 53 ms. Beats 50.42% of users with Python3 👎.
    Memory 16.59 MB. Beats 77.09% of users with Python3 👍.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        o = nums[:]
        c = 2
        for i in range(2, len(o)):
            if not (o[i] == o[i - 1] == o[i - 2]):
                nums[c] = o[i]
                c += 1
        return c


TEST_CASES = [
    ([1,1,1,2,2,3], [1,1,2,2,3], 5),  # noqa
    ([0,0,1,1,1,1,2,3,3], [0,0,1,1,2,3,3], 7),  # noqa
]


@pytest.mark.parametrize("nums, expected_nums, expected_k", TEST_CASES)
def test_Solution1(nums, expected_nums, expected_k):
    n = nums[:]
    k = Solution1().removeDuplicates(n)
    assert k == expected_k
    assert sorted(n[:k]) == sorted(expected_nums)


@pytest.mark.parametrize("nums, expected_nums, expected_k", TEST_CASES)
def test_Solution2(nums, expected_nums, expected_k):
    n = nums[:]
    k = Solution2().removeDuplicates(n)
    assert k == expected_k
    assert sorted(n[:k]) == sorted(expected_nums)
