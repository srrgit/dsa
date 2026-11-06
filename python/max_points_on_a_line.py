# 149. Max Points on a Line (Hard)
# Given an array of 2D points, return the maximum number of points that lie on
# the same straight line.
#
# Approach: for each point, compute the slope (as a reduced (dx, dy) fraction)
# to every other point and count how many share the same slope through that
# point (handling duplicate points and vertical lines separately). The best
# count seen across all pivot points is the answer. O(n^2) time, O(n) space.

from typing import List
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        best = 1
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 0
            local_best = 0
            x1, y1 = points[i]
            for j in range(n):
                if j == i:
                    continue
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slopes[(dx, dy)] += 1
                local_best = max(local_best, slopes[(dx, dy)])
            best = max(best, local_best + duplicates + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
    assert sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
    assert sol.maxPoints([[0, 0]]) == 1
    print("All tests passed.")
