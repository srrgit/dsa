# 1091. Shortest Path in Binary Matrix (Medium)
# Given an n x n binary grid, find the length of the shortest clear path from top-left to
# bottom-right, moving in any of the 8 directions through cells valued 0, counting the number
# of visited cells; return -1 if no such path exists.
# Approach: BFS from the start cell (8-directional), since all edges have equal weight.
# Time O(n^2), space O(n^2).

from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        if n == 1:
            return 1

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        queue = deque([(0, 0, 1)])

        while queue:
            r, c, dist = queue.popleft()
            if r == n - 1 and c == n - 1:
                return dist
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))
        return -1


if __name__ == "__main__":
    assert Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2
    assert Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert Solution().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    print("All tests passed.")
