# 93. Restore IP Addresses (Medium)
# Given a string s containing only digits, return all possible valid IP address
# combinations that can be formed by inserting dots into s.
# Approach: backtracking over the 4 segments, trying segment lengths 1-3 at each step and
# validating range/leading-zero rules. Branching is bounded by 3^4, so effectively O(1)
# time and space beyond the output.

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []
        segments = []

        def valid(segment: str) -> bool:
            if len(segment) == 0 or len(segment) > 3:
                return False
            if segment[0] == '0' and len(segment) > 1:
                return False
            return int(segment) <= 255

        def backtrack(start: int) -> None:
            if len(segments) == 4:
                if start == n:
                    result.append('.'.join(segments))
                return
            for length in range(1, 4):
                end = start + length
                if end > n:
                    break
                segment = s[start:end]
                if valid(segment):
                    segments.append(segment)
                    backtrack(end)
                    segments.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    assert sorted(Solution().restoreIpAddresses("25525511135")) == sorted(["255.255.11.135", "255.255.111.35"])
    assert Solution().restoreIpAddresses("0000") == ["0.0.0.0"]
    assert Solution().restoreIpAddresses("101023") != []
    print("All tests passed.")
