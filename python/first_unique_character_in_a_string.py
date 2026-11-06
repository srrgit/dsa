# 387. First Unique Character in a String (Easy)
# Given a string s, find the index of its first non-repeating character, or return -1 if
# every character repeats.
# Approach: count character frequencies in one pass, then scan again to find the first
# character whose count is 1. Time O(n), space O(1) (bounded alphabet).

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1


if __name__ == "__main__":
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("loveleetcode") == 2
    assert Solution().firstUniqChar("aabb") == -1
    print("All tests passed.")
