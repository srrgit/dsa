# 242. Valid Anagram (Easy)
# Given two strings s and t, return True if t is an anagram of s (same characters, same multiset
# of counts).
# Approach: compare character frequency counts.
# Time: O(n), Space: O(1) (bounded alphabet).

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    assert sol.isAnagram("a", "a") is True
    print("All tests passed.")
