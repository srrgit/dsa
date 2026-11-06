# 373. Find K Pairs with Smallest Sums (Medium)
# Given two sorted integer arrays `nums1` and `nums2` and an integer `k`,
# return the k pairs (u, v) with u from nums1 and v from nums2 that have the
# smallest sums.
#
# Approach: min-heap seeded with (nums1[i] + nums2[0], i, 0) for each i (up to
# k entries), then repeatedly pop the smallest-sum pair and push the next
# candidate in nums2 for that same nums1 index. O(k log k) time, O(k) space.

from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        result = []
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3) == [[1, 2], [1, 4], [1, 6]]
    assert sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 2) == [[1, 1], [1, 1]]
    print("All tests passed.")
