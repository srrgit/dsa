# 62. Unique Paths (Medium)
# A robot on an m x n grid starts at the top-left and can move only down or right. Return the
# number of distinct paths to reach the bottom-right corner.
# Approach: DP where dp[c] = number of ways to reach column c in the current row, built from the
# recurrence dp[r][c] = dp[r-1][c] + dp[r][c-1], using a rolling 1D array.
# Time: O(m*n), Space: O(n).

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(1, 1) == 1
    print("All tests passed.")
