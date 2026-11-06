# 1920. Build Array from Permutation (Easy)
# Given a zero-indexed permutation `nums`, build and return an array `ans` of
# the same length where ans[i] = nums[nums[i]].
#
# Approach: direct construction with a list comprehension. O(n) time, O(n)
# space (required for the output).

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


if __name__ == "__main__":
    sol = Solution()
    assert sol.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]
    assert sol.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]
    print("All tests passed.")
