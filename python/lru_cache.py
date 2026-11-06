# 146. LRU Cache (Medium)
# Design a Least Recently Used (LRU) cache that supports get and put in O(1) average time,
# evicting the least recently used entry whenever capacity is exceeded.
# Approach: an OrderedDict acts as both the hash map and the recency ordering; move_to_end on
# every access/insert marks an entry as most-recently-used, and popitem(last=False) evicts the
# least-recently-used entry.
# Time: O(1) per operation, Space: O(capacity).

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("All tests passed.")
