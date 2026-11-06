# 162. Find Peak Element (Medium)
# A peak element is strictly greater than its neighbors. Given an integer
# array nums, find a peak element's index (array ends are treated as
# -infinity). There may be multiple peaks; return the index of any one.
#
# Approach: binary search. Compare the middle element with its right
# neighbor; if nums[mid] < nums[mid+1], a peak must exist to the right, so
# search [mid+1, hi], otherwise search [lo, mid]. Time: O(log n),
# Space: O(1).

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    sol = Solution()
    assert sol.findPeakElement([1, 2, 3, 1]) == 2
    result = sol.findPeakElement([1, 2, 1, 3, 5, 6, 4])
    assert result in (1, 5)
    assert sol.findPeakElement([1]) == 0
    print("All test cases passed for 162. Find Peak Element")
