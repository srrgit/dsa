# 153. Find Minimum in Rotated Sorted Array (Medium)
# Given a sorted array of distinct integers that has been rotated between
# 1 and n times, return the minimum element without scanning the whole
# array.
#
# Approach: binary search. Compare nums[mid] to nums[hi]: if nums[mid] >
# nums[hi], the minimum lies strictly to the right of mid, otherwise it is
# at mid or to its left. Time: O(log n), Space: O(1).

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == "__main__":
    sol = Solution()
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert sol.findMin([11, 13, 15, 17]) == 11
    print("All test cases passed for 153. Find Minimum in Rotated Sorted Array")
