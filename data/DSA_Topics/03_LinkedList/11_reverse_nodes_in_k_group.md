# 11. Reverse Nodes in k-Group

**Topic**: LinkedList  
**Difficulty**: Hard  
**Tags**: Linked List, Recursion

---

## Problem Statement

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

---

## Input & Output Format

- **Input**: Head of linked list and an integer `k`.
- **Output**: Head of modified linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [1, 2, 3, 4, 5], k = 2
```

**Output:**
```text
[2, 1, 4, 3, 5]
```

**Explanation:**
Reversing groups of 2: (1, 2)->(2, 1), (3, 4)->(4, 3), 5 remains unchanged.

### Example 2

**Input:**
```text
head = [1, 2, 3, 4, 5], k = 3
```

**Output:**
```text
[3, 2, 1, 4, 5]
```

**Explanation:**
Reversing group of 3: (1, 2, 3)->(3, 2, 1), (4, 5) remain unchanged.

### Example 3

**Input:**
```text
head = [1, 2], k = 2
```

**Output:**
```text
[2, 1]
```

**Explanation:**
Reversing entire group of 2.

---

## Constraints

- The number of nodes in the list is `n`.
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
