# 128. Longest Consecutive Sequence (Medium)
# Given an unsorted array of integers, return the length of the longest run of consecutive
# integers that all appear in the array.
# Approach: put all numbers into a set for O(1) lookup; for each number that starts a sequence
# (i.e., num - 1 is not in the set), walk forward counting how many consecutive successors exist.
# Time: O(n) (each sequence is only walked once, from its start), Space: O(n).

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                best = max(best, length)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert sol.longestConsecutive([]) == 0
    print("All tests passed.")
