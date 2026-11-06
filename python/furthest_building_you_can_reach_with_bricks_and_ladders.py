# 1642. Furthest Building You Can Reach With Bricks and Ladders (Medium)
# Given building `heights`, a number of `bricks`, and a number of `ladders`,
# starting at building 0, moving to the next building costs (if taller)
# heights[i+1]-heights[i] either in bricks or by using a ladder. Return the
# furthest building index you can reach.
#
# Approach: greedily use ladders on the largest climbs. Walk the buildings,
# push each positive climb onto a min-heap of size <= ladders; when the heap
# would exceed `ladders`, pop its smallest climb and pay for it with bricks
# instead (since the ladder is better spent on a bigger climb). If bricks run
# out, stop. O(n log(ladders)) time, O(ladders) space.

from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # min-heap of climbs currently "paid" with ladders
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heapq.heappush(heap, climb)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1


if __name__ == "__main__":
    sol = Solution()
    assert sol.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1) == 4
    assert sol.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7
    assert sol.furthestBuilding([14, 3, 19, 3], 17, 0) == 3
    print("All tests passed.")
