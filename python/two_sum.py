# 1. Two Sum (Easy)
# Given an array of integers nums and an integer target, return the indices of the
# two numbers in nums that add up to target. Each input has exactly one solution,
# and you may not use the same element twice.
# Approach: single pass hash map from value -> index; for each num check if
# target - num was already seen. Time O(n), Space O(n).

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(sol.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(sol.twoSum([3, 3], 6)) == [0, 1]
    print("All tests passed.")
