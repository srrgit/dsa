# 213. House Robber II (Medium)
# Houses are arranged in a circle; adjacent houses cannot both be robbed. Given the amount of
# money in each house, return the maximum amount that can be robbed.
# Approach: the circle constraint means house 0 and house n-1 cannot both be taken, so run the
# classic linear House Robber DP twice: once excluding the last house, once excluding the
# first, and take the max. Time O(n), space O(1).

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            prev, curr = 0, 0
            for money in houses:
                prev, curr = curr, max(curr, prev + money)
            return curr

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == "__main__":
    assert Solution().rob([2, 3, 2]) == 3
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([1, 2, 3]) == 3
    print("All tests passed.")
