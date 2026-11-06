# 286. Walls and Gates (Medium)
#
# Given an m x n grid where -1 is a wall, 0 is a gate, and INF (2**31 - 1) is
# an empty room, fill each empty room with the distance to its nearest gate
# (unreachable rooms stay INF).
#
# Approach: multi-source BFS. Push all gates into the queue at once and
# expand outward simultaneously -- the first time a room is reached it's
# necessarily via the nearest gate, since all sources start at distance 0
# together.
# Time: O(m*n). Space: O(m*n) for the queue in the worst case.

from collections import deque
from typing import List

INF = 2147483647


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    sol.wallsAndGates(grid)
    for row in grid:
        print(row)
