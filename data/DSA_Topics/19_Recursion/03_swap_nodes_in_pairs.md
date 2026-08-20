# 3. Swap Nodes in Pairs

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: Linked List, Recursion

---

## Problem Statement

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed).

---

## Input & Output Format

- **Input**: Head node of singly linked list.
- **Output**: Head node of modified linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [1, 2, 3, 4]
```

**Output:**
```text
[2, 1, 4, 3]
```

**Explanation:**
(1, 2) swapped to (2, 1); (3, 4) swapped to (4, 3).

### Example 2

**Input:**
```text
head = []
```

**Output:**
```text
[]
```

**Explanation:**
Empty list.

### Example 3

**Input:**
```text
head = [1]
```

**Output:**
```text
[1]
```

**Explanation:**
Single node remains [1].

---

## Constraints

- The number of nodes in the list is in the range `[0, 100]`.
- `0 <= Node.val <= 100`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N) recursion stack`
