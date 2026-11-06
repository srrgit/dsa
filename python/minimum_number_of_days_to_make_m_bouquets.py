# 1482. Minimum Number of Days to Make m Bouquets (Medium)
# `bloomDay[i]` is the day flower i blooms. You need `m` bouquets, each using
# `k` *adjacent* bloomed flowers. Return the minimum number of days needed to
# make m bouquets, or -1 if impossible.
#
# Approach: binary search on the answer (the day). For a candidate day, greedily
# scan the flowers left-to-right counting adjacent runs of bloomed flowers to see
# how many bouquets of size k can be made; feasibility is monotonic in day.
# O(n log(max_day)) time, O(1) extra space.

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def can_make(day: int) -> bool:
            bouquets = 0
            run = 0
            for bloom in bloomDay:
                if bloom <= day:
                    run += 1
                    if run == k:
                        bouquets += 1
                        run = 0
                else:
                    run = 0
            return bouquets >= m

        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    sol = Solution()
    assert sol.minDays([1, 10, 3, 10, 2], 3, 1) == 3
    assert sol.minDays([1, 10, 3, 10, 2], 3, 2) == -1
    assert sol.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3) == 12
    print("All tests passed.")
