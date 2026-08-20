# 12. Lowest Common Ancestor of a Binary Tree

**Topic**: Binary Tree  
**Difficulty**: Medium  
**Tags**: Tree, Depth-First Search, Binary Tree

---

## Problem Statement

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes `p` and `q`.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**)."

---

## Input & Output Format

- **Input**: Binary tree root `root`, node `p`, and node `q`.
- **Output**: The LCA node.

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
```

**Output:**
```text
3
```

**Explanation:**
The LCA of nodes 5 and 1 is 3.

### Example 2

**Input:**
```text
root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
```

**Output:**
```text
5
```

**Explanation:**
The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself.

### Example 3

**Input:**
```text
root = [1, 2], p = 1, q = 2
```

**Output:**
```text
1
```

**Explanation:**
LCA of root 1 and child 2 is 1.

---

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the tree.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(H)`
