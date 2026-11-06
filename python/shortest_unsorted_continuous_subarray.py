# 581. Shortest Unsorted Continuous Subarray (Medium)
# Given an integer array, find the shortest contiguous subarray that, if sorted in place,
# would make the whole array sorted in ascending order. Return the length of that subarray
# (0 if the array is already sorted).
# Approach: scan left-to-right tracking the running max to find the rightmost position that is
# smaller than some earlier max (defines the right boundary); scan right-to-left tracking the
# running min to find the leftmost position that is larger than some later min (left
# boundary). Time O(n), space O(1).

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = -1, -2
        max_seen, min_seen = float("-inf"), float("inf")

        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                right = i

        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                left = i

        return right - left + 1


if __name__ == "__main__":
    assert Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert Solution().findUnsortedSubarray([1, 2, 3, 4]) == 0
    assert Solution().findUnsortedSubarray([1]) == 0
    print("All tests passed.")
