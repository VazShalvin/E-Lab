# 9. Validate Binary Search Tree

**Topic**: Binary Tree  
**Difficulty**: Medium  
**Tags**: Tree, Depth-First Search, Binary Search Tree, Binary Tree

---

## Problem Statement

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:
- The left subtree of a node contains only nodes with keys **strictly less** than the node's key.
- The right subtree of a node contains only nodes with keys **strictly greater** than the node's key.
- Both the left and right subtrees must also be binary search trees.

---

## Input & Output Format

- **Input**: Root of binary tree.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [2, 1, 3]
```

**Output:**
```text
true
```

**Explanation:**
Left child (1) < 2 and right child (3) > 2. Valid BST.

### Example 2

**Input:**
```text
root = [5, 1, 4, null, null, 3, 6]
```

**Output:**
```text
false
```

**Explanation:**
The root node's value is 5 but its right child's value is 4, which violates BST property.

### Example 3

**Input:**
```text
root = [10, 5, 15, null, null, 6, 20]
```

**Output:**
```text
false
```

**Explanation:**
Node 6 is in right subtree of 10 but is smaller than 10.

---

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(H)`
