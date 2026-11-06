# 131. Palindrome Partitioning (Medium)
# Given a string s, partition it such that every substring of the partition is a
# palindrome, and return all possible palindrome partitions.
# Approach: backtracking, trying every prefix at each position and recursing on the
# remainder when the prefix is a palindrome. Time O(n * 2^n) worst case, space O(n) recursion.

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        path = []

        def is_pal(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int) -> None:
            if start == n:
                result.append(path[:])
                return
            for end in range(start + 1, n + 1):
                sub = s[start:end]
                if is_pal(sub):
                    path.append(sub)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    assert Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert Solution().partition("a") == [["a"]]
    print("All tests passed.")
