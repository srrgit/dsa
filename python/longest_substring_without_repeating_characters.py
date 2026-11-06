# 3. Longest Substring Without Repeating Characters (Medium)
# Given a string s, find the length of the longest substring without repeating
# characters.
# Approach: sliding window with a dict mapping character -> last seen index; move
# the left boundary past the previous occurrence when a repeat is found.
# Time O(n), Space O(min(n, charset size)).


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    print("All tests passed.")
