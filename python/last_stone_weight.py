# 1046. Last Stone Weight (Easy)
# Given an array of stone weights, repeatedly smash the two heaviest stones together (replacing
# both with the absolute difference of their weights, or removing both if their weights are
# equal) until at most one stone remains. Return the weight of the last remaining stone, or 0 if
# none remain.
# Approach: a max-heap (simulated with a min-heap of negated values) to always extract the two
# heaviest stones efficiently.
# Time: O(n log n), Space: O(n).

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            diff = first - second
            if diff > 0:
                heapq.heappush(heap, -diff)

        return -heap[0] if heap else 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert sol.lastStoneWeight([1]) == 1
    assert sol.lastStoneWeight([2, 2]) == 0
    print("All tests passed.")
