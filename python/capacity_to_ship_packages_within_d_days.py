# 1011. Capacity To Ship Packages Within D Days (Medium)
# Given package `weights` (shipped in order, each day's packages load
# consecutively onto a ship without exceeding its capacity) and `days`, find
# the minimum ship capacity that lets all packages ship within `days` days.
#
# Approach: binary search on capacity between max(weights) and sum(weights).
# For a candidate capacity, greedily simulate loading days needed; feasibility
# is monotonic in capacity. O(n log(sum(weights))) time, O(1) space.

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_needed(capacity: int) -> int:
            needed = 1
            current = 0
            for w in weights:
                if current + w > capacity:
                    needed += 1
                    current = 0
                current += w
            return needed

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if days_needed(mid) <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    sol = Solution()
    assert sol.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert sol.shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6
    assert sol.shipWithinDays([1, 2, 3, 1, 1], 4) == 3
    print("All tests passed.")
