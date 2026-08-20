# 7. Number of Connected Components in an Undirected Graph

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Depth-First Search, Breadth-First Search, Union Find, Graph

---

## Problem Statement

You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [a_i, b_i]` indicates that there is an edge between `a_i` and `b_i` in the graph.

Return the number of connected components in the graph.

---

## Input & Output Format

- **Input**: An integer `n` and a 2D array `edges`.
- **Output**: An integer representing the count of connected components.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 5, edges = [[0, 1], [1, 2], [3, 4]]
```

**Output:**
```text
2
```

**Explanation:**
Components are {0, 1, 2} and {3, 4}.

### Example 2

**Input:**
```text
n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
```

**Output:**
```text
1
```

**Explanation:**
All nodes belong to one single component.

### Example 3

**Input:**
```text
n = 3, edges = []
```

**Output:**
```text
3
```

**Explanation:**
No edges, so each node forms its own component.

---

## Constraints

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= a_i <= b_i < n`
- `a_i != b_i`
- There are no duplicate edges.

---

## Complexity Analysis

- **Time Complexity**: `O(V + E)`
- **Space Complexity**: `O(V + E)`
