# 432. All O`one Data Structure (Hard)
#
# Design a structure supporting inc(key), dec(key), getMaxKey(), and
# getMinKey(), all in average O(1) time. getMaxKey/getMinKey return any key
# with the current max/min count, or "" if the structure is empty.
#
# Approach: maintain a doubly linked list of "buckets," each holding one
# distinct count value and the set of keys currently at that count, kept
# sorted ascending from head to tail. Two hashmaps give O(1) lookup:
# key -> count and count -> bucket node. On inc/dec, move a key from its
# current bucket to the adjacent bucket for the new count (creating that
# bucket right next to the current one if it doesn't exist, and deleting the
# old bucket if it becomes empty). Because the new bucket is always inserted
# immediately next to the current one, the list stays sorted without ever
# needing to search. getMaxKey/getMinKey just peek at the bucket next to
# tail/head.
# Time: O(1) average per operation. Space: O(k) for k distinct keys.

from collections import OrderedDict


class Node:
    __slots__ = ('count', 'keys', 'prev', 'next')

    def __init__(self, count):
        self.count = count
        self.keys = OrderedDict()  # acts as an ordered set of keys
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.key_count = {}
        self.count_node = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after(self, node, count):
        new_node = Node(count)
        nxt = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = nxt
        nxt.prev = new_node
        self.count_node[count] = new_node
        return new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node[node.count]

    def inc(self, key: str) -> None:
        cur_count = self.key_count.get(key, 0)
        new_count = cur_count + 1
        self.key_count[key] = new_count

        new_node = self.count_node.get(new_count)
        if new_node is None:
            base = self.head if cur_count == 0 else self.count_node[cur_count]
            new_node = self._insert_after(base, new_count)
        new_node.keys[key] = True

        if cur_count > 0:
            cur_node = self.count_node[cur_count]
            del cur_node.keys[key]
            if not cur_node.keys:
                self._remove(cur_node)

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return
        cur_count = self.key_count[key]
        cur_node = self.count_node[cur_count]

        if cur_count == 1:
            del self.key_count[key]
        else:
            new_count = cur_count - 1
            self.key_count[key] = new_count
            new_node = self.count_node.get(new_count)
            if new_node is None:
                new_node = self._insert_after(cur_node.prev, new_count)
            new_node.keys[key] = True

        del cur_node.keys[key]
        if not cur_node.keys:
            self._remove(cur_node)

    def getMaxKey(self) -> str:
        return "" if self.tail.prev is self.head else next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        return "" if self.head.next is self.tail else next(iter(self.head.next.keys))


if __name__ == "__main__":
    ao = AllOne()
    ao.inc("hello")
    ao.inc("hello")
    print(ao.getMaxKey())  # "hello"
    print(ao.getMinKey())  # "hello"
    ao.inc("leet")
    print(ao.getMaxKey())  # "hello"
    print(ao.getMinKey())  # "leet"
