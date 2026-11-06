# 237. Delete Node in a Linked List (Easy)
# You are given a node (not the head, and not the tail) of a singly linked
# list to delete, but you do NOT have access to the head of the list. Delete
# the node by modifying it in place.
#
# Approach: since we can't relink the previous node, we instead copy the next
# node's value into the given node and then skip over the next node (point
# this node's `next` to next.next). This effectively "removes" the given node
# from the list's perspective. O(1) time, O(1) space.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node: 'ListNode') -> None:
        node.val = node.next.val
        node.next = node.next.next


def build_list(values):
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()

    head = build_list([4, 5, 1, 9])
    node_to_delete = head.next  # node with val 5
    sol.deleteNode(node_to_delete)
    assert to_list(head) == [4, 1, 9]

    head2 = build_list([4, 5, 1, 9])
    node_to_delete2 = head2.next.next  # node with val 1
    sol.deleteNode(node_to_delete2)
    assert to_list(head2) == [4, 5, 9]
    print("All tests passed.")
