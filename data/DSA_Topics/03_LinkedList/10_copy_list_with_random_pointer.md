# 10. Copy List with Random Pointer

**Topic**: LinkedList  
**Difficulty**: Medium  
**Tags**: Hash Table, Linked List

---

## Problem Statement

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a **deep copy** of the list. Return the head of the copied linked list.

---

## Input & Output Format

- **Input**: Head of linked list with random pointers.
- **Output**: Head of cloned deep copied linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
```

**Output:**
```text
[[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
```

**Explanation:**
Deep copy has completely new nodes with identical connections.

### Example 2

**Input:**
```text
head = [[1, 1], [2, 1]]
```

**Output:**
```text
[[1, 1], [2, 1]]
```

**Explanation:**
Nodes point to copied nodes in new memory.

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
Empty list clone is null.

---

## Constraints

- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or is pointing to some node in the linked list.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) extra space without hash map`
