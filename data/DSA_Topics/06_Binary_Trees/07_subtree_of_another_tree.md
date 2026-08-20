# 7. Subtree of Another Tree

**Topic**: Binary Tree  
**Difficulty**: Easy  
**Tags**: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function

---

## Problem Statement

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

---

## Input & Output Format

- **Input**: Two binary tree roots `root` and `subRoot`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [3, 4, 5, 1, 2, null, null], subRoot = [4, 1, 2]
```

**Output:**
```text
true
```

**Explanation:**
The subtree rooted at node 4 in root is identical to subRoot.

### Example 2

**Input:**
```text
root = [3, 4, 5, 1, 2, null, null, null, null, 0], subRoot = [4, 1, 2]
```

**Output:**
```text
false
```

**Explanation:**
Node 2 in root has a child 0, whereas subRoot's node 2 has no child.

### Example 3

**Input:**
```text
root = [1, 1], subRoot = [1]
```

**Output:**
```text
true
```

**Explanation:**
Any leaf node 1 matches subRoot [1].

---

## Constraints

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(H)`
