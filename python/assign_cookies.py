# 455. Assign Cookies (Easy)
# Each child i has a greed factor g[i] (minimum cookie size that satisfies
# them) and each cookie j has a size s[j]. Each child gets at most one cookie.
# Maximize the number of satisfied children.
#
# Approach: greedy. Sort both `g` and `s`; walk through sorted cookies, and
# whenever the current cookie is big enough to satisfy the current least-greedy
# unsatisfied child, assign it and advance the child pointer. O(n log n + m log
# m) time, O(1) extra space.

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        for cookie in s:
            if child < len(g) and g[child] <= cookie:
                child += 1
        return child


if __name__ == "__main__":
    sol = Solution()
    assert sol.findContentChildren([1, 2, 3], [1, 1]) == 1
    assert sol.findContentChildren([1, 2], [1, 2, 3]) == 2
    print("All tests passed.")
