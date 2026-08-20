# 6. Graph Valid Tree

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Depth-First Search, Breadth-First Search, Union Find, Graph

---

## Problem Statement

Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

---

## Input & Output Format

- **Input**: An integer `n` and a 2D array `edges`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
```

**Output:**
```text
true
```

**Explanation:**
Has exactly 4 edges, no cycles, and is fully connected -> valid tree.

### Example 2

**Input:**
```text
n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
```

**Output:**
```text
false
```

**Explanation:**
Contains a cycle between 1, 2, and 3.

### Example 3

**Input:**
```text
n = 4, edges = [[0, 1], [2, 3]]
```

**Output:**
```text
false
```

**Explanation:**
Disconnected graph (2 components).

---

## Constraints

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- There are no duplicate edges.

---

## Complexity Analysis

- **Time Complexity**: `O(V + E)`
- **Space Complexity**: `O(V + E)`
