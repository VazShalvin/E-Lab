# 7. Linked List Cycle II (Find Start of Cycle)

**Topic**: LinkedList  
**Difficulty**: Medium  
**Tags**: Hash Table, Linked List, Two Pointers

---

## Problem Statement

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Do not modify the linked list.

---

## Input & Output Format

- **Input**: Head of linked list and pos.
- **Output**: Reference to node where cycle begins, or null.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [3, 2, 0, -4], pos = 1
```

**Output:**
```text
tail connects to node index 1
```

**Explanation:**
There is a cycle in the linked list, where tail connects to the node with value 2.

### Example 2

**Input:**
```text
head = [1, 2], pos = 0
```

**Output:**
```text
tail connects to node index 0
```

**Explanation:**
Cycle begins at node with value 1.

### Example 3

**Input:**
```text
head = [1], pos = -1
```

**Output:**
```text
no cycle
```

**Explanation:**
There is no cycle in the linked list.

---

## Constraints

- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
