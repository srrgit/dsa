# 137. Single Number II (Medium)
# Given an integer array where every element appears exactly three times
# except for one which appears exactly once, find that single element.
#
# Approach: bitwise digital-circuit trick using two accumulator variables
# (`ones`, `twos`) that track, per bit, whether we've seen it an odd number of
# times modulo 3. After processing all numbers, `ones` holds the answer.
# O(n) time, O(1) space.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones


if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNumber([2, 2, 3, 2]) == 3
    assert sol.singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99
    print("All tests passed.")
