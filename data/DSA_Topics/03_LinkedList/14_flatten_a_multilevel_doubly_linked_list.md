# 14. Flatten a Multilevel Doubly Linked List

**Topic**: LinkedList  
**Difficulty**: Medium  
**Tags**: Linked List, Depth-First Search, Doubly-Linked List

---

## Problem Statement

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional **child pointer**. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the `head` of the first level of the list.

---

## Input & Output Format

- **Input**: Head of multilevel doubly linked list.
- **Output**: Head of flattened single-level doubly linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [1, 2, 3, 4, 5, 6, null, null, null, 7, 8, 9, 10, null, null, 11, 12]
```

**Output:**
```text
[1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]
```

**Explanation:**
The multilevel list is flattened in pre-order depth-first traversal order.

### Example 2

**Input:**
```text
head = [1, 2, null, 3]
```

**Output:**
```text
[1, 3, 2]
```

**Explanation:**
Child list [3] is spliced after node 1.

### Example 3

**Input:**
```text
head = []
```

**Output:**
```text
[]
```

**Explanation:**
Empty list returns null/empty.

---

## Constraints

- The number of Nodes will not exceed `1000`.
- `1 <= Node.val <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) extra space`
