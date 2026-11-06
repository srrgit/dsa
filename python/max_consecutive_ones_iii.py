# 1004. Max Consecutive Ones III (Medium)
# Given a binary array nums and an integer k, return the maximum number of consecutive 1s in
# the array if you may flip at most k 0s to 1s.
# Approach: sliding window that tracks the number of zeros inside it; grow the right edge
# each step, and whenever the zero count exceeds k, shrink from the left until it's within
# budget again. Time O(n), space O(1).

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        best = 0

        for right, value in enumerate(nums):
            if value == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)

        return best


if __name__ == "__main__":
    assert Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10
    print("All tests passed.")
