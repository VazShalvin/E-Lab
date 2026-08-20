# 8. Construct Binary Tree from Preorder and Inorder Traversal

**Topic**: Binary Tree  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Divide and Conquer, Tree, Binary Tree

---

## Problem Statement

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

---

## Input & Output Format

- **Input**: Two integer arrays `preorder` and `inorder`.
- **Output**: Root of reconstructed binary tree.

---

## Sample Test Cases

### Example 1

**Input:**
```text
preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
```

**Output:**
```text
[3, 9, 20, null, null, 15, 7]
```

**Explanation:**
Root is 3. Inorder splits into left subtree [9] and right subtree [15, 20, 7].

### Example 2

**Input:**
```text
preorder = [-1], inorder = [-1]
```

**Output:**
```text
[-1]
```

**Explanation:**
Single node binary tree.

### Example 3

**Input:**
```text
preorder = [1, 2], inorder = [2, 1]
```

**Output:**
```text
[1, 2]
```

**Explanation:**
1 is root, 2 is left child.

---

## Constraints

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of unique values.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
