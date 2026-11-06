# 377. Combination Sum IV (Medium)
# Given a distinct-integer array `nums` and an integer `target`, return the
# number of possible (order-matters) combinations that add up to target.
#
# Approach: 1-D DP where dp[t] = number of ways to make sum t, dp[0] = 1, and
# dp[t] = sum(dp[t - num] for num in nums if num <= t). This is really counting
# ordered sequences (like a "staircase with steps nums"). O(target * len(nums))
# time, O(target) space.

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for num in nums:
                if num <= t:
                    dp[t] += dp[t - num]
        return dp[target]


if __name__ == "__main__":
    sol = Solution()
    assert sol.combinationSum4([1, 2, 3], 4) == 7
    assert sol.combinationSum4([9], 3) == 0
    assert sol.combinationSum4([1], 1) == 1
    print("All tests passed.")
