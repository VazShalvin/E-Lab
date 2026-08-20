# 3. Invert Binary Tree

**Topic**: Binary Tree  
**Difficulty**: Easy  
**Tags**: Tree, Depth-First Search, Breadth-First Search, Binary Tree

---

## Problem Statement

Given the `root` of a binary tree, invert the tree, and return its root.

---

## Input & Output Format

- **Input**: Root of binary tree `root`.
- **Output**: Root of inverted binary tree.

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [4, 2, 7, 1, 3, 6, 9]
```

**Output:**
```text
[4, 7, 2, 9, 6, 3, 1]
```

**Explanation:**
Left and right subtrees at every level are swapped.

### Example 2

**Input:**
```text
root = [2, 1, 3]
```

**Output:**
```text
[2, 3, 1]
```

**Explanation:**
1 and 3 are swapped.

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
Inverting empty tree gives empty tree.

---

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(H)`
