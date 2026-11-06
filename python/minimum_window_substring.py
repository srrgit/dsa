# 76. Minimum Window Substring (Hard)
# Given strings s and t, return the minimum window substring of s such that every
# character in t (including duplicates) is included in the window. Return "" if
# no such substring exists.
# Approach: sliding window with a need-count dict and a counter of how many
# distinct required characters are currently satisfied; expand right, then shrink
# left while still valid, tracking the best window. Time O(|s| + |t|), Space O(|t|).

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        missing = len(t)
        best_len = float("inf")
        best_start = 0
        left = 0

        for right, ch in enumerate(s, 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if right - left < best_len:
                    best_len = right - left
                    best_start = left
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    print("All tests passed.")
