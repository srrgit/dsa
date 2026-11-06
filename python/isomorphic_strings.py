# 205. Isomorphic Strings (Easy)
# Given two strings s and t of the same length, determine if the characters in s can be
# replaced to get t, with a consistent one-to-one mapping (no two characters map to the same
# character, and the mapping is consistent throughout).
# Approach: maintain two hash maps, one from s-characters to t-characters and one the reverse,
# verifying each new pair is consistent with (or extends) both mappings. Time O(n), space O(1)
# (bounded alphabet).


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for cs, ct in zip(s, t):
            if cs in s_to_t and s_to_t[cs] != ct:
                return False
            if ct in t_to_s and t_to_s[ct] != cs:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs

        return True


if __name__ == "__main__":
    assert Solution().isIsomorphic("egg", "add") is True
    assert Solution().isIsomorphic("foo", "bar") is False
    assert Solution().isIsomorphic("paper", "title") is True
    print("All tests passed.")
