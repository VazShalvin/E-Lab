# 3. Merge Two Sorted Lists

**Topic**: LinkedList  
**Difficulty**: Easy  
**Tags**: Linked List, Recursion

---

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

---

## Input & Output Format

- **Input**: Two heads of sorted linked lists `list1` and `list2`.
- **Output**: Head of the merged sorted linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
list1 = [1, 2, 4], list2 = [1, 3, 4]
```

**Output:**
```text
[1, 1, 2, 3, 4, 4]
```

**Explanation:**
Nodes are spliced in ascending numerical order.

### Example 2

**Input:**
```text
list1 = [], list2 = []
```

**Output:**
```text
[]
```

**Explanation:**
Merging two empty lists yields [].

### Example 3

**Input:**
```text
list1 = [], list2 = [0]
```

**Output:**
```text
[0]
```

**Explanation:**
Merging empty list with [0] yields [0].

---

## Constraints

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

---

## Complexity Analysis

- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(1)`
