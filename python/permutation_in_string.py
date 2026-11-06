# 567. Permutation in String (Medium)
# Given strings s1 and s2, return True if s2 contains a permutation of s1 as a contiguous
# substring.
# Approach: fixed-size sliding window of length len(s1) over s2, tracking character counts and
# comparing against s1's count array. Time O(len(s2)), space O(1) (26-letter alphabet).

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        need = Counter(s1)
        window = Counter(s2[:n1])
        if window == need:
            return True

        for i in range(n1, n2):
            window[s2[i]] += 1
            left_char = s2[i - n1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if window == need:
                return True
        return False


if __name__ == "__main__":
    assert Solution().checkInclusion("ab", "eidbaooo") is True
    assert Solution().checkInclusion("ab", "eidboaoo") is False
    assert Solution().checkInclusion("adc", "dcda") is True
    print("All tests passed.")
