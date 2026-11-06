# 211. Design Add and Search Words Data Structure (Medium)
# Design a data structure that supports adding words and searching whether a string matches any
# previously added word, where a '.' in the search query can match any single letter.
# Approach: a trie (prefix tree) stores added words. Search performs DFS over trie nodes along the
# query, branching over every child when a '.' is encountered.
# Time: O(L) per addWord; O(26^D * L) worst case per search, where D = number of dots and
# L = word length. Space: O(total characters stored).

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            ch = word[i]
            if ch == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                child = node.children.get(ch)
                if not child:
                    return False
                return dfs(child, i + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True
    print("All tests passed.")
