# 695. Max Area of Island (Medium)
# Given a binary grid representing a map of 1s (land) and 0s (water), return the maximum
# area of an island, where an island is formed by connecting adjacent 1s horizontally or
# vertically.
# Approach: DFS flood fill from every unvisited land cell, marking visited cells and
# counting cells per island, tracking the maximum. Time O(rows*cols), space O(rows*cols)
# for the recursion stack in the worst case.

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area


if __name__ == "__main__":
    grid1 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    assert Solution().maxAreaOfIsland(grid1) == 6

    grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert Solution().maxAreaOfIsland(grid2) == 0
    print("All tests passed.")
