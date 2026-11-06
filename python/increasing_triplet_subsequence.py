# 334. Increasing Triplet Subsequence (Medium)
# Given an integer array nums, return true if there exist three indices
# i < j < k such that nums[i] < nums[j] < nums[k].
#
# Approach: track the smallest value seen (first) and the smallest value
# seen that is greater than first (second) while scanning left to right.
# If a later number exceeds second, a valid increasing triplet exists.
# Time: O(n), Space: O(1).

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert sol.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert sol.increasingTriplet([2, 1, 5, 0, 4, 6]) is True
    print("All test cases passed for 334. Increasing Triplet Subsequence")
