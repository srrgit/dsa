# 383. Ransom Note (Easy)
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed
# using the letters from magazine, where each letter in magazine can only be used once.
# Approach: count letter frequencies in magazine, then compare against the required
# counts for ransomNote, failing if any count is insufficient. Time O(n + m), space O(1)
# (bounded alphabet).

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        note_count = Counter(ransomNote)
        for ch, cnt in note_count.items():
            if mag_count[ch] < cnt:
                return False
        return True


if __name__ == "__main__":
    assert Solution().canConstruct("a", "b") == False
    assert Solution().canConstruct("aa", "ab") == False
    assert Solution().canConstruct("aa", "aab") == True
    print("All tests passed.")
