# 218. The Skyline Problem (Hard)
# Given buildings as triples [left, right, height], return the skyline formed by
# these buildings as a list of "key points" [x, height] in left-to-right order,
# where each point represents a change in height.
# Approach: sweep-line over critical x-coordinates (building edges). At a left
# edge, push (-height, right) into a max-heap of "active" buildings; at each
# x-coordinate, pop buildings from the heap whose right edge is at or before the
# current x, then compare the current max active height to the last recorded
# height and emit a key point on change. Time O(n log n), Space O(n).

import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted({b[0] for b in buildings} | {b[1] for b in buildings})
        result = []
        heap = []  # (-height, right_edge)
        i = 0
        n = len(buildings)
        buildings_sorted = sorted(buildings, key=lambda b: b[0])
        prev_height = 0

        for x in events:
            while i < n and buildings_sorted[i][0] <= x:
                left, right, height = buildings_sorted[i]
                heapq.heappush(heap, (-height, right))
                i += 1
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)
            cur_height = -heap[0][0] if heap else 0
            if cur_height != prev_height:
                result.append([x, cur_height])
                prev_height = cur_height

        return result


if __name__ == "__main__":
    sol = Solution()
    buildings1 = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    expected1 = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    assert sol.getSkyline(buildings1) == expected1

    buildings2 = [[0, 2, 3], [2, 5, 3]]
    expected2 = [[0, 3], [5, 0]]
    assert sol.getSkyline(buildings2) == expected2
    print("All tests passed.")
