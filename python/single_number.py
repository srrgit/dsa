# 136. Single Number (Easy)
# Given a non-empty array of integers where every element appears twice except
# for one, find that single one.
# Approach: XOR all numbers together; identical values cancel out (x ^ x == 0),
# leaving only the unique value. Time O(n), Space O(1).

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNumber([2, 2, 1]) == 1
    assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
    assert sol.singleNumber([1]) == 1
    print("All tests passed.")
