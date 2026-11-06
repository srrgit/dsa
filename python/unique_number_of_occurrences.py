# 1207. Unique Number of Occurrences (Easy)
# Given an array of integers, return True if the number of occurrences of each
# distinct value in the array is unique.
#
# Approach: count occurrences with a Counter, then check that the multiset of
# counts has no duplicates (len(set(counts)) == len(counts)). O(n) time, O(n)
# space.

from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr).values()
        return len(set(counts)) == len(counts)


if __name__ == "__main__":
    sol = Solution()
    assert sol.uniqueOccurrences([1, 2, 2, 1, 1, 3]) is True
    assert sol.uniqueOccurrences([1, 2]) is False
    assert sol.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) is True
    print("All tests passed.")
