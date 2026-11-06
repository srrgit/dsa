# 472. Concatenated Words (Hard)
# Given a list of distinct words, return all words that can be formed by concatenating two or
# more other words from the same list.
# Approach: put all words in a set for O(1) lookups, then for each word run a word-break style
# DP (can_form): dp[i] is True if the prefix word[:i] can be built from pieces in the set.
# Exclude the single split that would match the ENTIRE word against itself, so a word is only
# accepted if it decomposes into two or more other words. Time ~O(sum(len(word)^2)), space
# O(max word length).

from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        result = []

        def can_form(word: str) -> bool:
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(i):
                    if j == 0 and i == n:
                        # Using the whole word as a single piece isn't a concatenation.
                        continue
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[n]

        for word in words:
            if word and can_form(word):
                result.append(word)
        return result


if __name__ == "__main__":
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses",
             "rat", "ratcatdogcat"]
    result = set(Solution().findAllConcatenatedWordsInADict(words))
    assert result == {"catsdogcats", "dogcatsdog", "ratcatdogcat"}

    words2 = ["cat", "dog", "catdog"]
    assert set(Solution().findAllConcatenatedWordsInADict(words2)) == {"catdog"}
    print("All tests passed.")
