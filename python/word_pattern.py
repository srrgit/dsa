# 290. Word Pattern (Easy)
# Given a pattern string and a string s, return true if s follows the same pattern, i.e.
# there is a bijection between letters of pattern and words of s.
# Approach: split s into words, check lengths match, then maintain two hashmaps for the
# forward (letter -> word) and backward (word -> letter) mappings, ensuring consistency
# in both directions. Time O(n), space O(n).

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}
        for ch, word in zip(pattern, words):
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            elif word in word_to_char:
                return False
            else:
                char_to_word[ch] = word
                word_to_char[word] = ch
        return True


if __name__ == "__main__":
    assert Solution().wordPattern("abba", "dog cat cat dog") == True
    assert Solution().wordPattern("abba", "dog cat cat fish") == False
    assert Solution().wordPattern("aaaa", "dog cat cat dog") == False
    print("All tests passed.")
