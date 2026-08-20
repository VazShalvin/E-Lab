# 7. Flatten Nested List Iterator (Recursive Generator)

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: Stack, Tree, Depth-First Search, Design, Queue, Iterator

---

## Problem Statement

You are given a nested list of integers `nestedList`. Each element is either an integer, or a list -- whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the `NestedIterator` class:
- `NestedIterator(List<NestedInteger> nestedList)` Initializes the iterator with the nested list `nestedList`.
- `int next()` Returns the next integer in the nested list.
- `boolean hasNext()` Returns `true` if there are still some integers in the nested list and `false` otherwise.

---

## Input & Output Format

- **Input**: A nested list of integers.
- **Output**: A flattened list of integers.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nestedList = [[1, 1], 2, [1, 1]]
```

**Output:**
```text
[1, 1, 2, 1, 1]
```

**Explanation:**
Flattened into a 1D sequence.

### Example 2

**Input:**
```text
nestedList = [1, [4, [6]]]
```

**Output:**
```text
[1, 4, 6]
```

**Explanation:**
Deeply nested lists unfolded.

### Example 3

**Input:**
```text
nestedList = []
```

**Output:**
```text
[]
```

**Explanation:**
Empty nested list.

---

## Constraints

- `1 <= nestedList.length <= 500`
- The values of the integers in the nested list are in the range `[-10^6, 10^6]`.

---

## Complexity Analysis

- **Time Complexity**: `O(1) amortized next/hasNext, O(N) traversal`
- **Space Complexity**: `O(D) where D is maximum nesting depth`
