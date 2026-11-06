# 139. Word Break (Medium)
# Given a string s and a list of words wordDict, determine if s can be
# segmented into a space-separated sequence of one or more dictionary words
# (words may be reused).
#
# Approach: dynamic programming. dp[i] is True if s[:i] can be segmented
# using dictionary words. dp[0] = True, and dp[i] = True if there exists a
# j < i with dp[j] True and s[j:i] in the word set.
# Time: O(n^2) (n = len(s), ignoring substring hashing cost),
# Space: O(n).

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    print("All test cases passed for 139. Word Break")
