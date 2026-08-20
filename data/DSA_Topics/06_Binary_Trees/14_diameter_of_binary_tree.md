# 14. Diameter of Binary Tree

**Topic**: Binary Tree  
**Difficulty**: Easy  
**Tags**: Tree, Depth-First Search, Binary Tree

---

## Problem Statement

Given the `root` of a binary tree, return the length of the **diameter** of the tree.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The length of a path between two nodes is represented by the number of edges between them.

---

## Input & Output Format

- **Input**: Root of binary tree `root`.
- **Output**: An integer representing the maximum path length in edges.

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [1, 2, 3, 4, 5]
```

**Output:**
```text
3
```

**Explanation:**
3 is the length of the path [4, 2, 1, 3] or [5, 2, 1, 3].

### Example 2

**Input:**
```text
root = [1, 2]
```

**Output:**
```text
1
```

**Explanation:**
Path between 1 and 2 has length 1.

### Example 3

**Input:**
```text
root = [1]
```

**Output:**
```text
0
```

**Explanation:**
Single node tree has diameter 0.

---

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(H)`
