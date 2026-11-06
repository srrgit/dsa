# 424. Longest Repeating Character Replacement (Medium)
# Given a string s and an integer k, you may replace up to k characters in the string with any
# other uppercase English letter. Return the length of the longest substring containing the same
# letter after performing such replacements.
# Approach: sliding window tracking letter frequency counts within the window. A window of length
# L is achievable if (L - count of its most frequent letter) <= k (i.e., at most k characters need
# changing). Shrink the window from the left whenever this is violated; the best window size never
# needs to shrink once achieved, so the max count can be tracked without decrementing on shrink.
# Time: O(n), Space: O(1) (26-letter alphabet).

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        max_count = 0
        best = 0

        for right, ch in enumerate(s):
            counts[ch] += 1
            max_count = max(max_count, counts[ch])

            window_len = right - left + 1
            if window_len - max_count > k:
                counts[s[left]] -= 1
                left += 1
            else:
                best = max(best, window_len)

        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AABABBA", 1) == 4
    assert sol.characterReplacement("AAAA", 0) == 4
    print("All tests passed.")
