# 1. Reverse Linked List

**Topic**: LinkedList  
**Difficulty**: Easy  
**Tags**: Linked List, Recursion

---

## Problem Statement

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

---

## Input & Output Format

- **Input**: Head node of singly linked list.
- **Output**: Head node of reversed linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [1, 2, 3, 4, 5]
```

**Output:**
```text
[5, 4, 3, 2, 1]
```

**Explanation:**
1->2->3->4->5 becomes 5->4->3->2->1.

### Example 2

**Input:**
```text
head = [1, 2]
```

**Output:**
```text
[2, 1]
```

**Explanation:**
1->2 becomes 2->1.

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
Reversing an empty list yields [].

---

## Constraints

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) iterative or O(N) recursive`
