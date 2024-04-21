"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List

import pytest


class Solution1:
    """First solution.

    Complexity: O(n)
    Memory complexity: O(1)
    Runtime: 686 ms. Beats 92.53% of users with Python3.
    Memory: 27.30 MB. Beats 72.00% of users with Python3
    """

    def maxProfit(self, prices: List[int]) -> int:
        start_val, range_max, total_max = prices[0], 0, 0

        for i in range(1, len(prices)):
            pi = prices[i]
            if pi <= start_val:
                if range_max > total_max:
                    total_max = range_max

                start_val = pi
                continue
            else:
                inc = pi - start_val
                if inc > range_max:
                    range_max = inc

        return max(total_max, range_max)


# class Solution2:
#     """In-place solution. Better algoritmically.

#     Complexity:
#     Memory complexity:
#     Runtime:
#     Memory:
#     """

TEST_CASES = [
    ([7,1,5,3,6,4], 5),  # noqa
    ([7,6,4,3,1], 0),  # noqa
    ([2,4,1], 2),  # noqa
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
