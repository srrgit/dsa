# 55. Jump Game (Medium)
# Given an array of non-negative integers nums where nums[i] is the maximum jump
# length from index i, determine if you can reach the last index starting from
# index 0.
# Approach: greedily track the farthest reachable index while scanning left to
# right; if the current index ever exceeds the farthest reachable point, it's
# unreachable and we return False. Time O(n), Space O(1).

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, num in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + num)
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.canJump([2, 3, 1, 1, 4]) is True
    assert sol.canJump([3, 2, 1, 0, 4]) is False
    assert sol.canJump([0]) is True
    print("All tests passed.")
