# 5. Remove Nth Node From End of List

**Topic**: LinkedList  
**Difficulty**: Medium  
**Tags**: Linked List, Two Pointers

---

## Problem Statement

Given the `head` of a linked list, remove the `n-th` node from the end of the list and return its head.

---

## Input & Output Format

- **Input**: Head of linked list `head` and an integer `n`.
- **Output**: Head of modified linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [1, 2, 3, 4, 5], n = 2
```

**Output:**
```text
[1, 2, 3, 5]
```

**Explanation:**
The 2nd node from the end is 4. Removing it gives 1->2->3->5.

### Example 2

**Input:**
```text
head = [1], n = 1
```

**Output:**
```text
[]
```

**Explanation:**
Removing the only node yields empty list.

### Example 3

**Input:**
```text
head = [1, 2], n = 1
```

**Output:**
```text
[1]
```

**Explanation:**
Removing the last node (2) leaves [1].

---

## Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
