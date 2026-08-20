# 15. LRU Cache Design (Doubly Linked List + HashMap)

**Topic**: LinkedList  
**Difficulty**: Medium  
**Tags**: Hash Table, Linked List, Design, Doubly-Linked List

---

## Problem Statement

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:
- `LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

---

## Input & Output Format

- **Input**: Operations: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
Arguments: [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
- **Output**: [null, null, null, 1, null, -1, null, -1, 3, 4]

---

## Sample Test Cases

### Example 1

**Input:**
```text
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1);
lRUCache.put(2, 2);
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // evicts key 2
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // evicts key 1
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

**Output:**
```text
[null, null, null, 1, null, -1, null, -1, 3, 4]
```

**Explanation:**
Key 2 is evicted when adding key 3 because key 1 was recently accessed. Key 1 is evicted when adding key 4.

### Example 2

**Input:**
```text
LRUCache lRUCache = new LRUCache(1);
lRUCache.put(2, 1);
lRUCache.get(2); // returns 1
lRUCache.put(3, 2); // evicts 2
lRUCache.get(2); // returns -1
```

**Output:**
```text
[null, null, 1, null, -1]
```

**Explanation:**
With capacity 1, every new insertion evicts the previous single entry.

### Example 3

**Input:**
```text
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(2, 1);
lRUCache.put(2, 2);
lRUCache.get(2); // returns 2
```

**Output:**
```text
[null, null, null, 2]
```

**Explanation:**
Updating an existing key updates its value and moves it to most recently used without eviction.

---

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls will be made to `get` and `put`.

---

## Complexity Analysis

- **Time Complexity**: `O(1) for both get and put`
- **Space Complexity**: `O(capacity)`
