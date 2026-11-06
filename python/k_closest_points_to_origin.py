# 973. K Closest Points to Origin (Medium)
# Given an array of points on the X-Y plane and an integer k, return the k closest
# points to the origin (0, 0), in any order.
# Approach: use a max-heap of size k keyed by negative squared distance (avoiding
# sqrt); push each point and pop the farthest whenever the heap exceeds size k.
# Time O(n log k), Space O(k).

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    sol = Solution()
    assert sol.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]

    res = sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert {tuple(p) for p in res} == {(3, 3), (-2, 4)}
    print("All tests passed.")
