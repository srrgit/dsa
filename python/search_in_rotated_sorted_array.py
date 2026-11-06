# 33. Search in Rotated Sorted Array (Medium)
# Given a rotated sorted array nums (originally ascending, rotated at some pivot)
# with distinct values, and a target value, return the index of target or -1 if
# not found.
# Approach: modified binary search; at each step determine which half (left or
# right of mid) is sorted, then decide which half target could be in based on
# comparisons with nums[lo] / nums[hi]. Time O(log n), Space O(1).

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:  # left half sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # right half sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([1], 0) == -1
    print("All tests passed.")
