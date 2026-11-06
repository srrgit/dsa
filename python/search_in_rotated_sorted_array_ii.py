# 81. Search in Rotated Sorted Array II (Medium)
# Given a rotated sorted array `nums` that may contain duplicates, and a
# `target`, return True if target exists in nums.
#
# Approach: modified binary search. At each step, if nums[lo] == nums[mid] ==
# ... we can't tell which half is sorted, so shrink the window by moving lo
# forward (skip the duplicate). Otherwise determine which half is properly
# sorted and decide which side to search as in the no-duplicates version.
# Average O(log n) time, worst case O(n) time (many duplicates), O(1) space.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] and nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert sol.search([2, 5, 6, 0, 0, 1, 2], 3) is False
    assert sol.search([1, 0, 1, 1, 1], 0) is True
    print("All tests passed.")
