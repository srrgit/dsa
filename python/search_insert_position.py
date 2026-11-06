# 35. Search Insert Position (Easy)
# Given a sorted array of distinct integers and a target value, return the
# index where target is found, or the index where it would be inserted to
# keep the array sorted.
#
# Approach: standard binary search for the leftmost insertion point
# (lower bound). Time: O(log n), Space: O(1).

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    sol = Solution()
    assert sol.searchInsert([1, 3, 5, 6], 5) == 2
    assert sol.searchInsert([1, 3, 5, 6], 2) == 1
    assert sol.searchInsert([1, 3, 5, 6], 7) == 4
    print("All test cases passed for 35. Search Insert Position")
