# 1838. Frequency of the Most Frequent Element (Medium)
# Given an array nums and an integer k, you may increment elements of nums at most k times in
# total (each operation adds 1 to one element). Return the maximum possible frequency of any
# element after these operations.
# Approach: sort the array, then use a sliding window [left, right]; the cost to make every
# element in the window equal to nums[right] is nums[right] * window_size - window_sum. Grow
# the window while that cost is <= k, shrinking from the left otherwise. Time O(n log n),
# space O(1).

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        best = 1
        for right in range(len(nums)):
            window_sum += nums[right]
            while nums[right] * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    assert Solution().maxFrequency([1, 2, 4], 5) == 3
    assert Solution().maxFrequency([1, 4, 8, 13], 5) == 2
    assert Solution().maxFrequency([3, 9, 6], 2) == 1
    print("All tests passed.")
