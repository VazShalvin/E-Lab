# 15. All Possible Full Binary Trees

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: Dynamic Programming, Tree, Recursion, Memoization, Binary Tree

---

## Problem Statement

Given an integer `n`, return a list of all possible **full binary trees** with `n` nodes. Each node of each tree in the answer must have `Node.val == 0`.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: A list of root nodes of all possible full binary trees.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 7
```

**Output:**
```text
5 distinct full binary trees
```

**Explanation:**
Can split nodes into left full tree of size i and right full tree of size n - 1 - i for odd i.

### Example 2

**Input:**
```text
n = 3
```

**Output:**
```text
1 distinct full binary tree: [0, 0, 0]
```

**Explanation:**
Root with 2 children.

### Example 3

**Input:**
```text
n = 2
```

**Output:**
```text
[]
```

**Explanation:**
No full binary tree can have an even number of nodes.

---

## Constraints

- `1 <= n <= 20`

---

## Complexity Analysis

- **Time Complexity**: `O(2^N / sqrt(N)) (Catalan number)`
- **Space Complexity**: `O(2^N)`
