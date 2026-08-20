# 14. Reorder List (Recursive Half Unfolding)

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: Linked List, Two Pointers, Recursion

---

## Problem Statement

Given a singly linked list `L: L0 → L1 → … → Ln-1 → Ln`, reorder it to: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …` using a recursive unfolding helper that pairs outward nodes.

---

## Input & Output Format

- **Input**: Head of singly linked list.
- **Output**: Head of reordered linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
head = [1, 2, 3, 4]
```

**Output:**
```text
[1, 4, 2, 3]
```

**Explanation:**
1 connects to 4, 4 to 2, 2 to 3.

### Example 2

**Input:**
```text
head = [1, 2, 3, 4, 5]
```

**Output:**
```text
[1, 5, 2, 4, 3]
```

**Explanation:**
Reordered correctly.

### Example 3

**Input:**
```text
head = [1]
```

**Output:**
```text
[1]
```

**Explanation:**
Single node unchanged.

---

## Constraints

- The number of nodes in the list is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N) recursion stack`
