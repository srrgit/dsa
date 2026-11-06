# 349. Intersection of Two Arrays (Easy)
# Given two integer arrays, return their intersection as an array of unique elements (each
# element appears at most once, order does not matter).
# Approach: convert both arrays to sets and intersect them. Time O(n + m), space O(n + m).

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    assert sorted(Solution().intersection([1, 2, 2, 1], [2, 2])) == [2]
    assert sorted(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
    print("All tests passed.")
