# 45. Jump Game II (Medium)
# Given an array nums where nums[i] represents the maximum jump length from
# index i, return the minimum number of jumps needed to reach the last
# index (it is guaranteed to be reachable).
#
# Approach: greedy BFS-style level expansion. Track the current jump's
# reachable boundary (`current_end`) and the farthest index reachable with
# one more jump (`farthest`) while scanning. Whenever the scan index
# reaches current_end, a new jump is required, so increment the jump
# count and update current_end to farthest. Time: O(n), Space: O(1).

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps


if __name__ == "__main__":
    sol = Solution()
    assert sol.jump([2, 3, 1, 1, 4]) == 2
    assert sol.jump([2, 3, 0, 1, 4]) == 2
    assert sol.jump([1, 1, 1, 1]) == 3
    print("All test cases passed for 45. Jump Game II")
