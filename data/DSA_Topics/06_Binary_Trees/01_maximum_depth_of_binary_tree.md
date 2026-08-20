# 1. Maximum Depth of Binary Tree

**Topic**: Binary Tree  
**Difficulty**: Easy  
**Tags**: Tree, Depth-First Search, Breadth-First Search, Binary Tree

---

## Problem Statement

Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## Input & Output Format

- **Input**: The root of a binary tree `root`.
- **Output**: An integer representing the maximum depth.

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [3, 9, 20, null, null, 15, 7]
```

**Output:**
```text
3
```

**Explanation:**
The longest path is 3 -> 20 -> 15 (or 7), which has 3 nodes.

### Example 2

**Input:**
```text
root = [1, null, 2]
```

**Output:**
```text
2
```

**Explanation:**
The path is 1 -> 2 with depth 2.

### Example 3

**Input:**
```text
root = []
```

**Output:**
```text
0
```

**Explanation:**
An empty tree has depth 0.

---

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(H) where H is tree height`
