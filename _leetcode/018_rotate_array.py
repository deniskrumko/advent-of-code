"""
https://leetcode.com/problems/rotate-array/
"""
from typing import List

import pytest


class Solution1:
    """First dumb solution.

    Complexity: O(n)
    Memory complexity: O(2n) -> O(n)

    Runtime: 152 ms. Beats 84.73% of users with Python3 👍
    Memory: 27.94 MB. Beats 69.78% of users with Python3 👍
    """

    def rotate(self, nums: List[int], k: int) -> None:
        total = len(nums)
        nums[:] = [nums[(i - k) % total] for i in range(total)]


TEST_CASES = [
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),  # noqa
    ([1,2,3,4,5,6,    7], 0, [1,2,3,4,5,6,7]),  # noqa
    ([-1,-100,3,99], 2, [3,99,-1,-100]),  # noqa
]


@pytest.mark.parametrize("nums, k, expected_nums", TEST_CASES)
def test_Solution1(nums, k, expected_nums):
    n = nums[:]
    Solution1().rotate(n, k)
    assert n == expected_nums
