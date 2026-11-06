# 452. Minimum Number of Arrows to Burst Balloons (Medium)
# Balloons are represented as horizontal diameters by [xstart, xend] pairs. An arrow shot
# at x bursts every balloon whose range includes x. Return the minimum arrows needed to
# burst all balloons.
# Approach: sort balloons by end coordinate, greedily shoot an arrow at the end of the
# first unburst balloon and skip every balloon that overlaps it. Time O(n log n), space O(1).

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda p: p[1])
        arrows = 1
        arrow_pos = points[0][1]
        for start, end in points[1:]:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end
        return arrows


if __name__ == "__main__":
    assert Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    print("All tests passed.")
