# 407. Trapping Rain Water II (Hard)
# Given an m x n integer matrix heightMap representing heights on a 2D terrain, return
# the total volume of rain water it can trap after raining.
# Approach: push all boundary cells into a min-heap, then repeatedly pop the lowest
# boundary cell, flooding each unvisited neighbor to at least the popped height and
# accumulating trapped water, pushing neighbors in with their effective (water) height.
# This is a variant of Dijkstra's algorithm. Time O(rows*cols*log(rows*cols)), space
# O(rows*cols).

from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        if rows < 3 or cols < 3:
            return 0

        visited = [[False] * cols for _ in range(rows)]
        heap = []

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        water = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            height, r, c = heapq.heappop(heap)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    water += max(0, height - heightMap[nr][nc])
                    heapq.heappush(heap, (max(height, heightMap[nr][nc]), nr, nc))
        return water


if __name__ == "__main__":
    heightMap1 = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    assert Solution().trapRainWater(heightMap1) == 4

    heightMap2 = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]
    assert Solution().trapRainWater(heightMap2) == 10
    print("All tests passed.")
