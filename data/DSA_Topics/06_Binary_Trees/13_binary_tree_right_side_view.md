# 13. Binary Tree Right Side View

**Topic**: Binary Tree  
**Difficulty**: Medium  
**Tags**: Tree, Depth-First Search, Breadth-First Search, Binary Tree

---

## Problem Statement

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return the values of the nodes you can see ordered from top to bottom.

---

## Input & Output Format

- **Input**: Root of binary tree `root`.
- **Output**: An array of integers visible from the right side.

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [1, 2, 3, null, 5, null, 4]
```

**Output:**
```text
[1, 3, 4]
```

**Explanation:**
From the right side, nodes 1, 3, and 4 are visible at each depth level.

### Example 2

**Input:**
```text
root = [1, null, 3]
```

**Output:**
```text
[1, 3]
```

**Explanation:**
Nodes 1 and 3 are visible.

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
Empty tree produces empty view.

---

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(H)`
