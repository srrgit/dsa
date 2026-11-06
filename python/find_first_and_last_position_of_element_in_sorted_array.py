# 34. Find First and Last Position of Element in Sorted Array (Medium)
# Given a sorted array `nums` and a `target`, return the starting and ending
# indices of target's occurrences, or [-1, -1] if not found.
#
# Approach: two binary searches - one for the leftmost insertion point of
# target, one for the leftmost insertion point of target+1 (= rightmost index
# of target + 1). O(log n) time, O(1) space.

from typing import List
import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target) - 1
        return [left, right]


if __name__ == "__main__":
    sol = Solution()
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert sol.searchRange([], 0) == [-1, -1]
    print("All tests passed.")
