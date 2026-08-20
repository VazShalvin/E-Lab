# 4. Map Sum Pairs

**Topic**: Trie  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Design, Trie

---

## Problem Statement

Design a map that allows you to do the following:
- Maps a string key to a given value.
- Sets a sum of the values that have a name with a prefix equal to a given string.

Implement the `MapSum` class:
- `MapSum()` Initializes the `MapSum` object.
- `void insert(String key, int val)` Inserts the `key-val` pair into the map. If the `key` already existed, the original `key-val` pair will be overridden to the new one.
- `int sum(String prefix)` Returns the sum of all the pairs' value whose `key` starts with the `prefix`.

---

## Input & Output Format

- **Input**: Method calls and parameters.
- **Output**: Output integers for sum calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple=3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple=3 + app=2)
```

**Output:**
```text
[null, null, 3, null, 5]
```

**Explanation:**
Prefix sum tracking maintained on each trie node.

### Example 2

**Input:**
```text
mapSum.insert("apple", 2); mapSum.sum("ap");
```

**Output:**
```text
[null, 4]
```

**Explanation:**
Updating existing key replaces its old value (app=2 + apple=2 = 4).

### Example 3

**Input:**
```text
mapSum.sum("banana");
```

**Output:**
```text
0
```

**Explanation:**
Prefix not found returns 0.

---

## Constraints

- `1 <= key.length, prefix.length <= 50`
- `key` and `prefix` consist of only lowercase English letters.
- `1 <= val <= 1000`
- At most `50` calls will be made to `insert` and `sum`.

---

## Complexity Analysis

- **Time Complexity**: `O(L) for insert and sum`
- **Space Complexity**: `O(Total Characters)`
