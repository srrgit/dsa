# 28. Find the Index of the First Occurrence in a String (Easy)
# Given strings `haystack` and `needle`, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Approach: KMP string matching. Build the needle's failure (longest
# proper prefix-suffix) table, then scan haystack once using it to avoid
# re-examining characters on a mismatch. O(n + m) time, O(m) space.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        # Build KMP failure table for needle.
        fail = [0] * m
        k = 0
        for i in range(1, m):
            while k > 0 and needle[i] != needle[k]:
                k = fail[k - 1]
            if needle[i] == needle[k]:
                k += 1
            fail[i] = k

        k = 0
        for i in range(n):
            while k > 0 and haystack[i] != needle[k]:
                k = fail[k - 1]
            if haystack[i] == needle[k]:
                k += 1
            if k == m:
                return i - m + 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.strStr("sadbutsad", "sad") == 0
    assert sol.strStr("leetcode", "leeto") == -1
    assert sol.strStr("hello", "ll") == 2
    print("All tests passed.")
