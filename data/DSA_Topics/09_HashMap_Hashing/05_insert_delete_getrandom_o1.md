# 5. Insert Delete GetRandom O(1)

**Topic**: HashMap / Hashing  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Math, Design, Randomized

---

## Problem Statement

Implement the `RandomizedSet` class:
- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if item not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions such that each function works in **average** `O(1)` time complexity.

---

## Input & Output Format

- **Input**: Method calls and parameters.
- **Output**: Outputs corresponding to method calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1, returns true
randomizedSet.remove(2); // Returns false as 2 is not in set
randomizedSet.insert(2); // Inserts 2, returns true
randomizedSet.getRandom(); // Returns 1 or 2 randomly
randomizedSet.remove(1); // Removes 1, returns true
randomizedSet.insert(2); // 2 already exists, returns false
randomizedSet.getRandom(); // Returns 2
```

**Output:**
```text
[null, true, false, true, 2, true, false, 2]
```

**Explanation:**
Combines a dynamic array and a hashmap to swap-and-pop for O(1) removals.

### Example 2

**Input:**
```text
rs.insert(10); rs.getRandom();
```

**Output:**
```text
[true, 10]
```

**Explanation:**
Only element 10 returned with probability 1.0.

### Example 3

**Input:**
```text
rs.insert(5); rs.remove(5);
```

**Output:**
```text
[true, true]
```

**Explanation:**
Successful insert and remove.

---

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`.

---

## Complexity Analysis

- **Time Complexity**: `O(1) average for all operations`
- **Space Complexity**: `O(N)`
