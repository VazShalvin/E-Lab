# 6. Reorder List

**Topic**: LinkedList  
**Difficulty**: Medium  
**Tags**: Linked List, Two Pointers, Stack

---

## Problem Statement

You are given the head of a singly linked-list:
`L0 → L1 → … → Ln - 1 → Ln`

Reorder the list to be on the following form:
`L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

---

## Input & Output Format

- **Input**: Head of singly linked list.
- **Output**: Modified head in reordered structure.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [1, 2, 3, 4]
```

**Output:**
```text
[1, 4, 2, 3]
```

**Explanation:**
Interleaving start and end nodes.

### Example 2

**Input:**
```text
head = [1, 2, 3, 4, 5]
```

**Output:**
```text
[1, 5, 2, 4, 3]
```

**Explanation:**
Reordered as L0->L4->L1->L3->L2.

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
Single node remains unchanged.

---

## Constraints

- The number of nodes in the list is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
