# 10. Kth Smallest Element in a BST

**Topic**: Binary Tree  
**Difficulty**: Medium  
**Tags**: Tree, Depth-First Search, Binary Search Tree, Binary Tree

---

## Problem Statement

Given the `root` of a binary search tree, and an integer `k`, return the `k-th` smallest value (**1-indexed**) of all the values of the nodes in the tree.

---

## Input & Output Format

- **Input**: Root of BST `root` and an integer `k`.
- **Output**: An integer value.

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [3, 1, 4, null, 2], k = 1
```

**Output:**
```text
1
```

**Explanation:**
Inorder traversal is [1, 2, 3, 4], 1st smallest is 1.

### Example 2

**Input:**
```text
root = [5, 3, 6, 2, 4, null, null, 1], k = 3
```

**Output:**
```text
3
```

**Explanation:**
Inorder traversal is [1, 2, 3, 4, 5, 6], 3rd smallest is 3.

### Example 3

**Input:**
```text
root = [2, 1, 3], k = 2
```

**Output:**
```text
2
```

**Explanation:**
2nd smallest is root value 2.

---

## Constraints

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(H + k)`
- **Space Complexity**: `O(H)`
