# 312. Burst Balloons (Hard)
# Given n balloons with values nums[i], bursting a balloon i yields nums[left] * nums[i] *
# nums[right] coins, where left/right are the currently adjacent balloons (treating out-of-
# bounds as value 1). Return the maximum coins obtainable by bursting all balloons.
# Approach: pad the array with 1s on both ends, then interval DP where dp[i][j] is the maximum
# coins obtainable from bursting all balloons strictly between indices i and j (exclusive),
# trying every possible LAST balloon k to burst in that range. Time O(n^3), space O(n^2).

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        n = len(balloons)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(0, n - length):
                j = i + length
                best = 0
                for k in range(i + 1, j):
                    coins = balloons[i] * balloons[k] * balloons[j] + dp[i][k] + dp[k][j]
                    best = max(best, coins)
                dp[i][j] = best

        return dp[0][n - 1]


if __name__ == "__main__":
    assert Solution().maxCoins([3, 1, 5, 8]) == 167
    assert Solution().maxCoins([1, 5]) == 10
    print("All tests passed.")
