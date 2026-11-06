# 448. Find All Numbers Disappeared in an Array (Easy)
# Given an array nums of n integers where each nums[i] is in the range [1, n], return all integers
# in [1, n] that do not appear in nums.
# Approach: use the array itself as a hash set by negating the value at index (|nums[i]| - 1) for
# each number visited; at the end, indices still holding a positive value correspond to missing
# numbers. Restore signs afterward to leave the input otherwise unchanged.
# Time: O(n), Space: O(1) extra.

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        result = [i + 1 for i, x in enumerate(nums) if x > 0]
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert sol.findDisappearedNumbers([1, 1]) == [2]
    assert sol.findDisappearedNumbers([1, 2, 3]) == []
    print("All tests passed.")
