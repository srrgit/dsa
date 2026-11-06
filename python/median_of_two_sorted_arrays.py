# 4. Median of Two Sorted Arrays (Hard)
# Given two sorted arrays nums1 and nums2, return the median of the combined
# sorted array, in O(log(m+n)) time.
# Approach: binary search for the correct partition point on the shorter array so
# that the combined left half and right half are balanced and every element on the
# left is <= every element on the right. Time O(log(min(m, n))), Space O(1).

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return float(min(right1, right2))
                return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1
        raise ValueError("Input arrays are not sorted properly")


if __name__ == "__main__":
    sol = Solution()
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert sol.findMedianSortedArrays([], [1]) == 1.0
    print("All tests passed.")
