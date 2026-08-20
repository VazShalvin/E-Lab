# 5. Binary Tree Level Order Traversal

**Topic**: Binary Tree  
**Difficulty**: Medium  
**Tags**: Tree, Breadth-First Search, Binary Tree

---

## Problem Statement

Given the `root` of a binary tree, return the *level order traversal* of its nodes' values (i.e., from left to right, level by level).

---

## Input & Output Format

- **Input**: Root of binary tree.
- **Output**: A 2D array of integers grouped by level.

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [3, 9, 20, null, null, 15, 7]
```

**Output:**
```text
[[3], [9, 20], [15, 7]]
```

**Explanation:**
Level 0: [3], Level 1: [9, 20], Level 2: [15, 7].

### Example 2

**Input:**
```text
root = [1]
```

**Output:**
```text
[[1]]
```

**Explanation:**
Single level with root node.

### Example 3

**Input:**
```text
root = []
```

**Output:**
```text
[]
```

**Explanation:**
Empty tree produces empty traversal.

---

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
