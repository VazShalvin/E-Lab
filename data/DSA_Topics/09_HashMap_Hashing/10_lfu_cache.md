# 10. LFU Cache Design

**Topic**: HashMap / Hashing  
**Difficulty**: Hard  
**Tags**: Hash Table, Linked List, Design, Doubly-Linked List

---

## Problem Statement

Design and implement a data structure for a **Least Frequently Used (LFU)** cache.

Implement the `LFUCache` class:
- `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.
- `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.
- `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used** key would be invalidated.

Functions `get` and `put` must run in `O(1)` average time complexity.

---

## Input & Output Format

- **Input**: Method calls and parameters.
- **Output**: Output list corresponding to get operations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1, cnt(1)=2
lfu.put(3, 3);   // 2 is evicted as cnt(2)=1 is min, cache=[3,1]
lfu.get(2);      // returns -1 (not found)
lfu.get(3);      // return 3, cnt(3)=2
lfu.put(4, 4);   // both 1 and 3 have cnt=2, 1 is least recently used so 1 is evicted, cache=[4,3]
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
lfu.get(4);      // return 4
```

**Output:**
```text
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]
```

**Explanation:**
Maintains frequency buckets mapped to doubly-linked lists for O(1) updates.

### Example 2

**Input:**
```text
LFUCache lfu = new LFUCache(0); lfu.put(0, 0); lfu.get(0);
```

**Output:**
```text
[null, null, -1]
```

**Explanation:**
Capacity 0 cannot store any key.

### Example 3

**Input:**
```text
LFUCache lfu = new LFUCache(1); lfu.put(2, 1); lfu.get(2);
```

**Output:**
```text
[null, null, 1]
```

**Explanation:**
Stores and retrieves key 2.

---

## Constraints

- `0 <= capacity <= 10^4`
- `0 <= key <= 10^5`
- `0 <= value <= 10^9`
- At most `2 * 10^5` calls will be made to `get` and `put`.

---

## Complexity Analysis

- **Time Complexity**: `O(1) for get and put`
- **Space Complexity**: `O(capacity)`
