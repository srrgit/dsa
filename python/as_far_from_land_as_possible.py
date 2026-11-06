# 1162. As Far from Land as Possible (Medium)
# Given an n x n binary grid where 1 = land and 0 = water, find a water cell
# such that its distance (Manhattan, moving in 4 directions through the grid)
# to the nearest land cell is maximized, and return that distance. Return -1
# if the grid has only land or only water.
#
# Approach: multi-source BFS starting from all land cells simultaneously; the
# last layer reached gives the maximum distance. O(n^2) time, O(n^2) space.

from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))

        if not queue or len(queue) == n * n:
            return -1

        visited = [[grid[r][c] == 1 for c in range(n)] for r in range(n)]
        distance = -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            distance += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        return distance


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2
    assert sol.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4
    assert sol.maxDistance([[1, 1], [1, 1]]) == -1
    print("All tests passed.")
