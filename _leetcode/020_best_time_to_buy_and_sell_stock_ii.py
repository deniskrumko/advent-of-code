"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

from typing import List

import pytest


class Solution1:
    """First dumb solution.

    Complexity: O(n)
    Memory complexity: O(1)
    Runtime: 56 ms. Beats 67.55% of users with Python3 👍
    Memory: 17.55 MB. Beats 73.37% of users with Python3 👍
    """

    def maxProfit(self, prices: List[int]) -> int:
        start_val, last_val, total_profit = prices[0], prices[0], 0

        for i in range(1, len(prices)):
            pi = prices[i]
            if pi <= last_val:
                total_profit += (last_val - start_val)
                start_val = pi

            last_val = pi

        total_profit += (last_val - start_val)
        return total_profit


# class Solution2:
#     """In-place solution. Better algoritmically.

#     Complexity:
#     Memory complexity:
#     Runtime:
#     Memory:
#     """


TEST_CASES = [
    ([7,1,5,3,6,4], 7),  # noqa
    ([1,2,3,4,5], 4),  # noqa
    ([7,6,4,3,1], 0),  # noqa
    ([6,1,3,2,4,7], 7),  # noqa
]


@pytest.mark.parametrize("prices, expected_profit", TEST_CASES)
def test_Solution1(prices, expected_profit):
    assert Solution1().maxProfit(prices) == expected_profit


# @pytest.mark.parametrize("nums, expected_nums, expected_k", TEST_CASES)
# def test_Solution2(nums, expected_nums, expected_k):
#     n = nums[:]
#     k = Solution2().removeDuplicates(n)
#     assert k == expected_k
#     assert sorted(n[:k]) == sorted(expected_nums)
