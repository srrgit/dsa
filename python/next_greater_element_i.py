# 496. Next Greater Element I (Easy)
# nums1 and nums2 are arrays of distinct integers, with nums1 a subset of nums2. For each
# element of nums1, find its next greater element to its right in nums2, or -1 if none exists.
# Approach: monotonic decreasing stack over nums2 to compute a "next greater" map in O(n) time,
# then O(m) lookups for nums1. Time O(n + m), space O(n).

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [next_greater.get(num, -1) for num in nums1]


if __name__ == "__main__":
    assert Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    print("All tests passed.")
