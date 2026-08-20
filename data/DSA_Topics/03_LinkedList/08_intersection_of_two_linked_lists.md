# 8. Intersection of Two Linked Lists

**Topic**: LinkedList  
**Difficulty**: Easy  
**Tags**: Hash Table, Linked List, Two Pointers

---

## Problem Statement

Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.

---

## Input & Output Format

- **Input**: Two heads of singly linked lists `headA` and `headB`.
- **Output**: Intersected node reference, or null.

---

## Sample Test Cases

### Example 1

**Input:**
```text
intersectVal = 8, listA = [4, 1, 8, 4, 5], listB = [5, 6, 1, 8, 4, 5]
```

**Output:**
```text
Intersected at '8'
```

**Explanation:**
The intersected node's value is 8.

### Example 2

**Input:**
```text
intersectVal = 2, listA = [1, 9, 1, 2, 4], listB = [3, 2, 4]
```

**Output:**
```text
Intersected at '2'
```

**Explanation:**
The intersected node's value is 2.

### Example 3

**Input:**
```text
intersectVal = 0, listA = [2, 6, 4], listB = [1, 5]
```

**Output:**
```text
No intersection
```

**Explanation:**
The two lists do not intersect, so return null.

---

## Constraints

- The number of nodes of `listA` is in the `m`.
- The number of nodes of `listB` is in the `n`.
- `1 <= m, n <= 3 * 10^4`
- `1 <= Node.val <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(1)`
