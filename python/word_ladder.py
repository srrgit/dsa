# 127. Word Ladder (Hard)
# Given a beginWord, an endWord, and a wordList, return the number of
# words in the shortest transformation sequence from beginWord to endWord,
# changing exactly one letter at a time, where each intermediate word must
# exist in wordList. Return 0 if no such sequence exists.
#
# Approach: BFS over the implicit graph where an edge connects two words
# differing by exactly one letter. From each word, generate all possible
# one-letter-changed variants and check membership in the word set (using
# a wildcard pattern isn't necessary at this scale, but generating 26
# variants per position is standard and efficient). Track visited words to
# avoid revisiting. Time: O(n * L^2) where n = number of words, L = word
# length (L for generating variants, * 26 constant for alphabet),
# Space: O(n * L).

from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue
                    candidate = word[:i] + c + word[i + 1:]
                    if candidate in word_set and candidate not in visited:
                        visited.add(candidate)
                        queue.append((candidate, steps + 1))
        return 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert sol.ladderLength("a", "c", ["a", "b", "c"]) == 2
    print("All test cases passed for 127. Word Ladder")
