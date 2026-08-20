# 15. Flatten Binary Tree to Linked List

**Topic**: Binary Tree  
**Difficulty**: Medium  
**Tags**: Linked List, Stack, Tree, Depth-First Search, Binary Tree

---

## Problem Statement

Given the `root` of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
- The "linked list" should be in the same order as a **pre-order traversal** of the binary tree.

---

## Input & Output Format

- **Input**: Root of binary tree.
- **Output**: Modified binary tree structured as a right-skewed list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [1, 2, 5, 3, 4, null, 6]
```

**Output:**
```text
[1, null, 2, null, 3, null, 4, null, 5, null, 6]
```

**Explanation:**
Flattened into right-linked pre-order: 1 -> 2 -> 3 -> 4 -> 5 -> 6.

### Example 2

**Input:**
```text
root = []
```

**Output:**
```text
[]
```

**Explanation:**
Empty tree remains empty.

### Example 3

**Input:**
```text
root = [0]
```

**Output:**
```text
[0]
```

**Explanation:**
Single node remains [0].

---

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) using Morris traversal or O(H) recursive`
