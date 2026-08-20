# 12. Time Based Key-Value Store

**Topic**: Binary Search  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Binary Search, Design

---

## Problem Statement

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:
- `TimeMap()` Initializes the object of the data structure.
- `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

---

## Input & Output Format

- **Input**: Method calls and parameters.
- **Output**: Output values corresponding to get calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
```

**Output:**
```text
[null, null, "bar", "bar", null, "bar2", "bar2"]
```

**Explanation:**
Binary search on timestamps for given key.

### Example 2

**Input:**
```text
timeMap.get("unknown", 1);
```

**Output:**
```text
""
```

**Explanation:**
Key not found returns empty string.

### Example 3

**Input:**
```text
timeMap.set("love", "high", 10); timeMap.get("love", 5);
```

**Output:**
```text
""
```

**Explanation:**
Query timestamp is earlier than smallest stored timestamp.

---

## Constraints

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits.
- `1 <= timestamp <= 10^7`
- All the timestamps of `set` are strictly increasing.

---

## Complexity Analysis

- **Time Complexity**: `O(1) set, O(log N) get`
- **Space Complexity**: `O(N)`
