# 49. Group Anagrams (Medium)
# Given an array of strings strs, group the anagrams together (in any order).
# Approach: use a dict keyed by each string's sorted-character tuple (a canonical
# form shared by all its anagrams); append each string to the list for its key.
# Time O(n * k log k) where k is the max string length, Space O(n * k).

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()
    res = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = sorted(sorted(g) for g in res)
    expected = sorted([sorted(["eat", "tea", "ate"]), sorted(["tan", "nat"]), ["bat"]])
    assert normalized == expected

    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]
    print("All tests passed.")
