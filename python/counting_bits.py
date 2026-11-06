# 338. Counting Bits (Easy)
# Given an integer n, return an array ans of length n + 1 such that
# ans[i] is the number of 1's (set bits) in the binary representation of i,
# for each 0 <= i <= n.
#
# Approach: dynamic programming using the relation
# ans[i] = ans[i >> 1] + (i & 1), since i >> 1 drops the lowest bit and
# (i & 1) tells us whether that dropped bit was a 1.
# Time: O(n), Space: O(n).

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert sol.countBits(2) == [0, 1, 1]
    assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert sol.countBits(0) == [0]
    print("All test cases passed for 338. Counting Bits")
