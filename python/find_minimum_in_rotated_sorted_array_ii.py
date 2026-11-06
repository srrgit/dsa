# 154. Find Minimum in Rotated Sorted Array II (Hard)
# Given a sorted array `nums` (possibly containing duplicates) that has been
# rotated at an unknown pivot, find the minimum element.
#
# Approach: modified binary search. If nums[mid] > nums[hi], the minimum is
# strictly to the right of mid, so lo = mid + 1. If nums[mid] < nums[hi], the
# minimum is at or to the left of mid, so hi = mid. If they're equal, we can't
# tell which side the minimum is on, so shrink the search space by hi -= 1.
# Average O(log n) time, worst case O(n) (all duplicates), O(1) space.

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[lo]


if __name__ == "__main__":
    sol = Solution()
    assert sol.findMin([1, 3, 5]) == 1
    assert sol.findMin([2, 2, 2, 0, 1]) == 0
    assert sol.findMin([1, 1]) == 1
    print("All tests passed.")
