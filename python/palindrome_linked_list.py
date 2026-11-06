# 234. Palindrome Linked List (Easy)
# Given the head of a singly linked list, return True if it is a palindrome.
# Approach: find the middle with slow/fast pointers, reverse the second half
# in-place, then compare the first half against the reversed second half.
# Time O(n), Space O(1).

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half starting at slow
        prev = None
        cur = slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        # Compare first half with reversed second half
        left, right = head, prev
        while right:  # right (reversed half) is the shorter or equal half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(build_list([1, 2, 2, 1])) is True
    assert sol.isPalindrome(build_list([1, 2])) is False
    assert sol.isPalindrome(build_list([1])) is True
    print("All tests passed.")
