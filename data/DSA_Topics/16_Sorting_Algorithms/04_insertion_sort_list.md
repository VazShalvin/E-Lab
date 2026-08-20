# 4. Insertion Sort List

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Linked List, Sorting

---

## Problem Statement

Given the `head` of a singly linked list, sort the list using **insertion sort**, and return the sorted list's head.

---

## Input & Output Format

- **Input**: Head node of singly linked list.
- **Output**: Head node of sorted linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [4, 2, 1, 3]
```

**Output:**
```text
[1, 2, 3, 4]
```

**Explanation:**
Insertion sort builds sorted list from left to right.

### Example 2

**Input:**
```text
head = [-1, 5, 3, 4, 0]
```

**Output:**
```text
[-1, 0, 3, 4, 5]
```

**Explanation:**
Sorted order.

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
Empty list returns empty.

---

## Constraints

- The number of nodes in the list is in the range `[1, 5000]`.
- `-5000 <= Node.val <= 5000`

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(1)`
