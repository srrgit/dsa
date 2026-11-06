# 215. Kth Largest Element in an Array (Medium)
# Given an integer array nums and an integer k, return the kth largest element in
# the array (counting from the largest, not necessarily distinct values).
# Approach: maintain a min-heap of size k; push every element and pop the smallest
# whenever the heap exceeds size k, leaving the kth largest at the heap's top.
# Time O(n log k), Space O(k).

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: List[int] = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


if __name__ == "__main__":
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert sol.findKthLargest([1], 1) == 1
    print("All tests passed.")
