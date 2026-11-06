# 347. Top K Frequent Elements (Medium)
# Given an integer array nums and an integer k, return the k most frequent
# elements, in any order.
# Approach: count frequencies with Counter, then use a heap (heapq.nlargest) keyed
# by frequency to pull the top k. Time O(n log k), Space O(n).

import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=counts.get)


if __name__ == "__main__":
    sol = Solution()
    assert set(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert sol.topKFrequent([1], 1) == [1]
    assert set(sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)) == {-1, 2}
    print("All tests passed.")
