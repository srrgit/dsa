# 329. Longest Increasing Path in a Matrix (Hard)
# Given an m x n integer matrix, return the length of the longest strictly
# increasing path, where moves are allowed in the four cardinal directions.
#
# Approach: DFS with memoization. memo[r][c] stores the longest increasing
# path starting at (r, c). For each cell, recursively explore neighbors with
# a strictly greater value and take 1 + the best neighbor result; cache to
# avoid recomputation. Each cell is computed once. Time: O(m*n),
# Space: O(m*n) for the memo table and recursion stack.

from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])

        memo = [[0] * cols for _ in range(rows)]

        def dfs(r: int, c: int) -> int:
            if memo[r][c] != 0:
                return memo[r][c]
            best = 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            memo[r][c] = best
            return best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert sol.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    assert sol.longestIncreasingPath([[1]]) == 1
    print("All test cases passed for 329. Longest Increasing Path in a Matrix")
