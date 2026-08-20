# 9. Add Two Numbers

**Topic**: LinkedList  
**Difficulty**: Medium  
**Tags**: Linked List, Math, Recursion

---

## Problem Statement

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

## Input & Output Format

- **Input**: Two heads of linked lists `l1` and `l2`.
- **Output**: Head of linked list representing the sum.

---

## Sample Test Cases

### Example 1

**Input:**
```text
l1 = [2, 4, 3], l2 = [5, 6, 4]
```

**Output:**
```text
[7, 0, 8]
```

**Explanation:**
342 + 465 = 807. In reverse order, [7, 0, 8].

### Example 2

**Input:**
```text
l1 = [0], l2 = [0]
```

**Output:**
```text
[0]
```

**Explanation:**
0 + 0 = 0.

### Example 3

**Input:**
```text
l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
```

**Output:**
```text
[8, 9, 9, 9, 0, 0, 0, 1]
```

**Explanation:**
9999999 + 9999 = 10009998.

---

## Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

---

## Complexity Analysis

- **Time Complexity**: `O(max(N, M))`
- **Space Complexity**: `O(max(N, M))`
