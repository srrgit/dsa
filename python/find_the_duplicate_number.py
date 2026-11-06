# 287. Find the Duplicate Number (Medium)
# Given an array of n+1 integers where each integer is in the range [1, n], there is
# exactly one repeated number (possibly repeated more than once); find it without
# modifying the array and using O(1) extra space.
# Approach: treat the array as a function i -> nums[i] inducing an implicit cycle, and use
# Floyd's cycle detection (tortoise and hare) to find the cycle's entrance, which is the
# duplicate value. Time O(n), space O(1).

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == "__main__":
    assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2
    assert Solution().findDuplicate([3, 1, 3, 4, 2]) == 3
    print("All tests passed.")
