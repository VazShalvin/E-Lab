# 2. Same Tree

**Topic**: Binary Tree  
**Difficulty**: Easy  
**Tags**: Tree, Depth-First Search, Breadth-First Search, Binary Tree

---

## Problem Statement

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

---

## Input & Output Format

- **Input**: Two binary tree roots `p` and `q`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
p = [1, 2, 3], q = [1, 2, 3]
```

**Output:**
```text
true
```

**Explanation:**
Both trees have the exact same structure and node values.

### Example 2

**Input:**
```text
p = [1, 2], q = [1, null, 2]
```

**Output:**
```text
false
```

**Explanation:**
Structures differ (left child vs right child).

### Example 3

**Input:**
```text
p = [1, 2, 1], q = [1, 1, 2]
```

**Output:**
```text
false
```

**Explanation:**
Node values differ across corresponding positions.

---

## Constraints

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(H)`
