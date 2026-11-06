# 746. Min Cost Climbing Stairs (Easy)
# Given an array `cost` where cost[i] is the cost of stepping on stair i, starting
# at index 0 or 1, find the minimum cost to reach the top (one step past the last
# index), moving one or two steps at a time.
#
# Approach: bottom-up DP where dp[i] = min cost to reach step i. dp[i] = cost[i] +
# min(dp[i-1], dp[i-2]). We only need the last two values, so O(n) time, O(1) space.

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp_prev2 / dp_prev1 = min cost to *reach* (stand on, before paying) stair i-2 / i-1
        dp_prev2, dp_prev1 = 0, 0
        for i in range(2, n + 1):
            dp_cur = min(dp_prev1 + cost[i - 1], dp_prev2 + cost[i - 2])
            dp_prev2, dp_prev1 = dp_prev1, dp_cur
        return dp_prev1


if __name__ == "__main__":
    sol = Solution()
    assert sol.minCostClimbingStairs([10, 15, 20]) == 15
    assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    print("All tests passed.")
