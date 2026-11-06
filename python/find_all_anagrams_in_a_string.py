# 438. Find All Anagrams in a String (Medium)
# Given strings `s` and `p`, return the start indices of all substrings of `s`
# that are anagrams of `p`.
#
# Approach: sliding window of length len(p) over s, maintaining a count array
# (or Counter) of the window and comparing to the count of p. O(n) time (n =
# len(s)), O(1) extra space (fixed 26-letter alphabet).

from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        p_count = Counter(p)
        window = Counter(s[:m])
        result = []
        if window == p_count:
            result.append(0)
        for i in range(m, n):
            window[s[i]] += 1
            left_char = s[i - m]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if window == p_count:
                result.append(i - m + 1)
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert sol.findAnagrams("abab", "ab") == [0, 1, 2]
    assert sol.findAnagrams("a", "ab") == []
    print("All tests passed.")
