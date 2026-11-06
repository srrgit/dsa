# 931. Minimum Falling Path Sum (Medium)
# Given an n x n integer matrix, a falling path starts at any element in the
# first row and chooses one element from each row, where the chosen element in
# the next row must be in a column that differs by at most 1 from the current
# column. Return the minimum sum of any falling path.
#
# Approach: bottom-up DP in place: for each row (after the first), each cell's
# new value becomes itself plus the min of the three reachable cells directly
# above it (above, above-left, above-right). The answer is the min of the
# last row. O(n^2) time, O(1) extra space (modifies matrix / O(n) if copied).

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]
        for r in range(1, n):
            new_dp = [0] * n
            for c in range(n):
                best_above = dp[c]
                if c > 0:
                    best_above = min(best_above, dp[c - 1])
                if c < n - 1:
                    best_above = min(best_above, dp[c + 1])
                new_dp[c] = matrix[r][c] + best_above
            dp = new_dp
        return min(dp)


if __name__ == "__main__":
    sol = Solution()
    assert sol.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    assert sol.minFallingPathSum([[-19, 57], [-40, -5]]) == -59
    print("All tests passed.")
