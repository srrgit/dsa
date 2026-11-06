# 14. Longest Common Prefix (Easy)
# Given an array of strings, find the longest common prefix shared by all
# of them. Return an empty string if there is no common prefix.
#
# Approach: take the first string as a candidate prefix and repeatedly trim
# it from the end until every other string starts with it. Time:
# O(S) where S is the sum of all characters (bounded by len(first) * n in
# the worst case), Space: O(1) extra (ignoring the returned string).

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert sol.longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters"
    print("All test cases passed for 14. Longest Common Prefix")
