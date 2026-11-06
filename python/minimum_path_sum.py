# 64. Minimum Path Sum (Medium)
# Given an m x n grid filled with non-negative numbers, find a path from top-left to
# bottom-right that minimizes the sum of numbers along the path, moving only right or down.
# Approach: dynamic programming where each cell holds the minimum path sum to reach it
# from the top-left, computed from the min of the cell above and the cell to the left.
# Time O(rows*cols), space O(rows*cols) (not mutating the input grid).

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [row[:] for row in grid]

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    dp[r][c] += dp[r][c - 1]
                elif c == 0:
                    dp[r][c] += dp[r - 1][c]
                else:
                    dp[r][c] += min(dp[r - 1][c], dp[r][c - 1])
        return dp[rows - 1][cols - 1]


if __name__ == "__main__":
    assert Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert Solution().minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    print("All tests passed.")
