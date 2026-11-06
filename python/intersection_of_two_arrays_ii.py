# 350. Intersection of Two Arrays II (Easy)
# Given two integer arrays `nums1` and `nums2`, return their intersection as an
# array; each element in the result should appear as many times as it shows in
# both arrays.
#
# Approach: count elements of the smaller array with a Counter, then scan the
# other array, emitting (and decrementing) matches. O(n + m) time, O(min(n, m))
# space.

from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        counts = Counter(nums1)
        result = []
        for num in nums2:
            if counts.get(num, 0) > 0:
                result.append(num)
                counts[num] -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.intersect([1, 2, 2, 1], [2, 2])) == [2, 2]
    assert sorted(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
    print("All tests passed.")
