# 1032. Stream of Characters (Hard)
# Design a class that receives characters one at a time (via `query`) and after
# each character returns True if some suffix of the characters seen so far forms
# a word present in a given dictionary `words`.
#
# Approach: build a trie of the *reversed* words. Keep a buffer of characters
# seen so far; on each query, walk the reversed-character stream backward
# through the trie checking for a completed word. Building the trie is
# O(sum len(words)); each query is O(longest word length) time.

from typing import List


class TrieNode:
    __slots__ = ("children", "is_word")

    def __init__(self):
        self.children = {}
        self.is_word = False


class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.max_len = 0
        for word in words:
            self.max_len = max(self.max_len, len(word))
            node = self.root
            for ch in reversed(word):
                node = node.children.setdefault(ch, TrieNode())
            node.is_word = True
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        if len(self.stream) > self.max_len:
            self.stream = self.stream[-self.max_len:]
        node = self.root
        for ch in reversed(self.stream):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_word:
                return True
        return False


if __name__ == "__main__":
    sc = StreamChecker(["cd", "f", "kl"])
    results = [sc.query(c) for c in "abcdefghijkl"]
    expected = [False, False, False, True, False, True, False, False, False, False, False, True]
    assert results == expected, results
    print("All tests passed.")
