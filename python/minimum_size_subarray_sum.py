# 209. Minimum Size Subarray Sum (Medium)
# Given an array of positive integers nums and a positive integer target, return the minimal
# length of a contiguous subarray whose sum is >= target, or 0 if no such subarray exists.
# Approach: sliding window — expand the right edge, accumulating the sum, and whenever the sum
# meets or exceeds target, shrink from the left while recording the minimum window length seen.
# Time O(n), space O(1).

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        best = float("inf")

        for right, value in enumerate(nums):
            window_sum += value
            while window_sum >= target:
                best = min(best, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if best == float("inf") else best


if __name__ == "__main__":
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3, 3]) == 2
    assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1
    assert Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    print("All tests passed.")
