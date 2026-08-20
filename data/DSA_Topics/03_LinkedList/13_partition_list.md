# 13. Partition List

**Topic**: LinkedList  
**Difficulty**: Medium  
**Tags**: Linked List, Two Pointers

---

## Problem Statement

Given the `head` of a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`.

You should preserve the original relative order of the nodes in each of the two partitions.

---

## Input & Output Format

- **Input**: Head of linked list and an integer `x`.
- **Output**: Head of partitioned linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [1, 4, 3, 2, 5, 2], x = 3
```

**Output:**
```text
[1, 2, 2, 4, 3, 5]
```

**Explanation:**
Nodes less than 3 are [1, 2, 2]; nodes >= 3 are [4, 3, 5]. Concatenated: [1, 2, 2, 4, 3, 5].

### Example 2

**Input:**
```text
head = [2, 1], x = 2
```

**Output:**
```text
[1, 2]
```

**Explanation:**
1 < 2, so 1 comes before 2.

### Example 3

**Input:**
```text
head = [1], x = 0
```

**Output:**
```text
[1]
```

**Explanation:**
All nodes >= 0, remains [1].

---

## Constraints

- The number of nodes in the list is in the range `[0, 200]`.
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
