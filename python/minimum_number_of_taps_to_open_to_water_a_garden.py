# 1326. Minimum Number of Taps to Open to Water a Garden (Hard)
# There is a garden represented as a 1D line of length n (positions 0..n).
# There are n+1 taps at each integer position i, and opening tap i waters the
# range [i - ranges[i], i + ranges[i]] (clipped to [0, n]). Return the minimum
# number of taps needed to water the entire garden [0, n], or -1 if
# impossible.
#
# Approach: convert each tap into an interval and reduce to the classic "jump
# game" / minimum interval-covering problem: for each left endpoint L, record
# the furthest right endpoint reachable from any tap starting at or before L
# (farthest[L] = max right coverage achievable starting the reach from L).
# Then greedily scan left to right like the minimum-jumps problem. O(n) time,
# O(n) space.

from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        farthest = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            farthest[left] = max(farthest[left], right)

        taps = 0
        current_end = 0
        next_end = 0
        i = 0
        while current_end < n:
            while i <= current_end:
                next_end = max(next_end, farthest[i])
                i += 1
            if next_end <= current_end:
                return -1
            taps += 1
            current_end = next_end
        return taps


if __name__ == "__main__":
    sol = Solution()
    assert sol.minTaps(5, [3, 4, 1, 1, 0, 0]) == 1
    assert sol.minTaps(3, [0, 0, 0, 0]) == -1
    assert sol.minTaps(7, [1, 2, 1, 0, 2, 1, 0, 1]) == 3
    print("All tests passed.")
