# 279. Perfect Squares (Medium)
# Given an integer n, return the least number of perfect square numbers that sum to n.
# Approach: dynamic programming where dp[i] is the minimum count for i, built up from
# dp[i - j*j] + 1 for every perfect square j*j <= i. Time O(n * sqrt(n)), space O(n).

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


if __name__ == "__main__":
    assert Solution().numSquares(12) == 3
    assert Solution().numSquares(13) == 2
    print("All tests passed.")
