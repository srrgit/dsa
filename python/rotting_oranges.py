# 994. Rotting Oranges (Medium)
# Given a grid where 0 = empty cell, 1 = fresh orange, 2 = rotten orange, every minute a rotten
# orange rots its 4-directionally adjacent fresh oranges. Return the minimum minutes until no
# fresh orange remains, or -1 if that is impossible.
# Approach: multi-source BFS starting from all rotten oranges simultaneously, advancing minute by
# minute (processing one BFS "layer" per minute).
# Time: O(m*n), Space: O(m*n).

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert sol.orangesRotting([[0, 2]]) == 0
    print("All tests passed.")
