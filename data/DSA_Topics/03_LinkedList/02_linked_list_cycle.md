# 2. Linked List Cycle (Detect Cycle)

**Topic**: LinkedList  
**Difficulty**: Easy  
**Tags**: Hash Table, Linked List, Two Pointers

---

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

---

## Input & Output Format

- **Input**: Head of linked list and pos (internal index).
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [3, 2, 0, -4], pos = 1
```

**Output:**
```text
true
```

**Explanation:**
There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

### Example 2

**Input:**
```text
head = [1, 2], pos = 0
```

**Output:**
```text
true
```

**Explanation:**
There is a cycle in the linked list, where the tail connects to the 0th node.

### Example 3

**Input:**
```text
head = [1], pos = -1
```

**Output:**
```text
false
```

**Explanation:**
There is no cycle in the linked list.

---

## Constraints

- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
