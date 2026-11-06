# 981. Time Based Key-Value Store (Medium)
# Design a time-based key-value store that stores multiple values for the same key at
# different timestamps, supporting set(key, value, timestamp) and get(key, timestamp)
# which returns the value with the largest recorded timestamp <= the given timestamp (or
# "" if there is none).
# Approach: store a list of (timestamp, value) pairs per key, appended in increasing
# timestamp order (as guaranteed by the problem), and binary search for the floor
# timestamp on get. set is O(1) amortized, get is O(log n).

from collections import defaultdict
from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store.get(key)
        if not entries:
            return ""
        idx = bisect_right(entries, (timestamp, chr(0x10FFFF))) - 1
        if idx < 0:
            return ""
        return entries[idx][1]


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"
    print("All tests passed.")
