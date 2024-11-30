"""
https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
"""

import pytest
from typing import List


class Solution1:
    """First dumb solution.

    Complexity:
    Memory complexity:
    Runtime: 3612 ms. Beats 9.97% of users with Python3 👎👎👎
    Memory: 409.91 MB. Beats 5.08% of users with Python3 👎👎👎
    """

    def canJump(self, nums: List[int], rshift: int = 1) -> bool:
        if (len(nums) - rshift) <= 1:
            return nums[0] > 0 or (len(nums) - rshift) <= 0

        for i in range(1, len(nums) - rshift + 1):
            if nums[-i - rshift] >= i:
                return self.canJump(nums, rshift=rshift + i)

        return False
    # def canJump(self, nums: List[int]) -> bool:
    #     if len(nums) <= 2:
    #         return nums[0] > 0 or len(nums) == 1

    #     for i in range(1, len(nums)):
    #         if nums[-i - 1] >= i:
    #             return self.canJump(nums[:-i])

    #     return False


# class Solution2:
#     """In-place solution. Better algoritmically.

#     Complexity:
#     Memory complexity:
#     Runtime:
#     Memory:
#     """

TEST_CASES = [
    ([2,3,1,1,4], True),  # noqa
    ([3,2,1,0,4], False),  # noqa
    ([3,2,1,0,4], False),  # noqa
    ([1], True),  # noqa
    ([0,1], False),  # noqa
    ([2,0,0], True),  # noqa
    ([1,0,2], False),  # noqa
]


@pytest.mark.parametrize("nums, expected", TEST_CASES)
def test_Solution1(nums, expected):
    assert Solution1().canJump(nums) == expected


# @pytest.mark.parametrize("nums, expected_nums, expected_k", TEST_CASES)
# def test_Solution2(nums, expected_nums, expected_k):
#     n = nums[:]
#     k = Solution2().removeDuplicates(n)
#     assert k == expected_k
#     assert sorted(n[:k]) == sorted(expected_nums)
