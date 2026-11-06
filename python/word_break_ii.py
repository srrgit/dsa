# 140. Word Break II (Hard)
# Given a string s and a dictionary of strings wordDict, add spaces to construct all
# possible sentences where each word is a valid dictionary word.
# Approach: backtracking with memoization keyed by starting index, caching the list of
# valid sentences for each suffix of s to avoid recomputation. Time O(2^n) worst case
# (heavily pruned in practice by memoization), space O(2^n) for stored results.

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        memo = {}

        def backtrack(start: int) -> List[str]:
            if start in memo:
                return memo[start]
            if start == n:
                return [""]
            sentences = []
            for end in range(start + 1, n + 1):
                word = s[start:end]
                if word in word_set:
                    for rest in backtrack(end):
                        sentences.append(word if rest == "" else word + " " + rest)
            memo[start] = sentences
            return sentences

        return backtrack(0)


if __name__ == "__main__":
    result = Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    assert sorted(result) == sorted(["cats and dog", "cat sand dog"])

    result2 = Solution().wordBreak("pineapplepenapple",
                                    ["apple", "pen", "applepen", "pine", "pineapple"])
    assert sorted(result2) == sorted(
        ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])

    result3 = Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert result3 == []
    print("All tests passed.")
