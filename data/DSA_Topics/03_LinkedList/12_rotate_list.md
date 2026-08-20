# 12. Rotate List

**Topic**: LinkedList  
**Difficulty**: Medium  
**Tags**: Linked List, Two Pointers

---

## Problem Statement

Given the `head` of a linked list, rotate the list to the right by `k` places.

---

## Input & Output Format

- **Input**: Head of linked list and an integer `k`.
- **Output**: Head of rotated linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [1, 2, 3, 4, 5], k = 2
```

**Output:**
```text
[4, 5, 1, 2, 3]
```

**Explanation:**
rotate 1 steps to the right: [5, 1, 2, 3, 4]
rotate 2 steps to the right: [4, 5, 1, 2, 3]

### Example 2

**Input:**
```text
head = [0, 1, 2], k = 4
```

**Output:**
```text
[2, 0, 1]
```

**Explanation:**
rotate 1 steps to the right: [2, 0, 1]
rotate 4 steps = 4 % 3 = 1 rotation.

### Example 3

**Input:**
```text
head = [], k = 0
```

**Output:**
```text
[]
```

**Explanation:**
Empty list rotation is empty list.

---

## Constraints

- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
