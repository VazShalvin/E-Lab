# 5. Sort List (Merge Sort on Linked List)

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort

---

## Problem Statement

Given the `head` of a linked list, return the list after sorting it in **ascending order** in `O(n log n)` time and `O(1)` extra space (ignoring recursion stack).

---

## Input & Output Format

- **Input**: Head of singly linked list.
- **Output**: Head of sorted linked list.

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
Divided into halves using fast/slow pointers, then merged.

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
Sorted linked list.

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

- The number of nodes in the list is in the range `[0, 5 * 10^4]`.
- `-10^5 <= Node.val <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(log N) or O(1) bottom-up`
