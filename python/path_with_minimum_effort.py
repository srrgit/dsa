# 1631. Path With Minimum Effort (Medium)
# Given a 2D grid of heights, find a path from the top-left to the bottom-right cell (moving
# in 4 directions) that minimizes the maximum absolute height difference between two
# consecutive cells on the path. Return that minimized effort.
# Approach: Dijkstra's algorithm where the "distance" to a cell is the minimum possible largest
# step taken to reach it; relax neighbors with max(current_effort, height_diff). Time
# O(rows*cols*log(rows*cols)), space O(rows*cols).

import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]  # (effort_so_far, row, col)

        while heap:
            curr_effort, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return curr_effort
            if curr_effort > effort[r][c]:
                continue
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(curr_effort, diff)
                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        return 0


if __name__ == "__main__":
    assert Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert Solution().minimumEffortPath(
        [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    ) == 0
    print("All tests passed.")
