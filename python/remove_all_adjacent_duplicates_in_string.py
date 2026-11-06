# 1047. Remove All Adjacent Duplicates In String (Easy)
# Given a string `s`, repeatedly remove adjacent pairs of equal letters until no
# such pair remains, and return the final string.
#
# Approach: use a stack; for each character, if it equals the top of the stack,
# pop it (cancel the pair), otherwise push it. O(n) time, O(n) space.


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeDuplicates("abbaca") == "ca"
    assert sol.removeDuplicates("azxxzy") == "ay"
    print("All tests passed.")
