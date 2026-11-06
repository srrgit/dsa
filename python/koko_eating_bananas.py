# 875. Koko Eating Bananas (Medium)
# Koko has piles of bananas and h hours to eat them all. Each hour she picks
# one pile and eats k bananas from it (if the pile has fewer than k, she
# finishes that pile and stops for the hour). Find the minimum integer
# eating speed k so she finishes all bananas within h hours.
#
# Approach: binary search on the answer k, ranging from 1 to max(piles).
# For a candidate speed, compute the total hours needed (ceil division per
# pile) and check feasibility against h. Time: O(n log(max(piles))),
# Space: O(1).

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        def hours_needed(speed: int) -> int:
            return sum(math.ceil(pile / speed) for pile in piles)

        while lo < hi:
            mid = (lo + hi) // 2
            if hours_needed(mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    sol = Solution()
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    print("All test cases passed for 875. Koko Eating Bananas")
