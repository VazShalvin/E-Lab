# 4. Binary Tree Maximum Path Sum

**Topic**: Binary Tree  
**Difficulty**: Hard  
**Tags**: Dynamic Programming, Tree, Depth-First Search, Binary Tree

---

## Problem Statement

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum **path sum** of any non-empty path.

---

## Input & Output Format

- **Input**: Root of binary tree.
- **Output**: An integer representing maximum path sum.

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [1, 2, 3]
```

**Output:**
```text
6
```

**Explanation:**
The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

### Example 2

**Input:**
```text
root = [-10, 9, 20, null, null, 15, 7]
```

**Output:**
```text
42
```

**Explanation:**
The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

### Example 3

**Input:**
```text
root = [-3]
```

**Output:**
```text
-3
```

**Explanation:**
Single node path sum is -3.

---

## Constraints

- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
- `-1000 <= Node.val <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(H)`
