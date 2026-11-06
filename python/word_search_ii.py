# 212. Word Search II (Hard)
# Given an m x n board of characters and a list of words, return all words from the list that can
# be constructed by sequentially adjacent cells on the board (horizontally or vertically
# neighboring), using each cell at most once per word.
# Approach: build a trie from all words, then run DFS from every board cell, walking the trie in
# lockstep with the board. When a trie node marks the end of a word, record it and clear that
# marker to avoid duplicate results; mark visited cells in place during DFS and restore them on
# backtrack, pruning trie branches with no remaining children as an optimization.
# Time: O(m*n*4^L) worst case, Space: O(sum of word lengths) for the trie.

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # holds the complete word at terminal nodes


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                node = node.children.setdefault(ch, TrieNode())
            node.word = w

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            child = node.children[ch]
            if child.word is not None:
                result.append(child.word)
                child.word = None  # avoid duplicates

            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, child)
            board[r][c] = ch

            if not child.children:
                node.children.pop(ch, None)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result


if __name__ == "__main__":
    sol = Solution()
    board1 = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words1 = ["oath", "pea", "eat", "rain"]
    assert sorted(sol.findWords([row[:] for row in board1], words1)) == ["eat", "oath"]

    board2 = [["a", "b"], ["c", "d"]]
    words2 = ["abcb"]
    assert sol.findWords([row[:] for row in board2], words2) == []
    print("All tests passed.")
