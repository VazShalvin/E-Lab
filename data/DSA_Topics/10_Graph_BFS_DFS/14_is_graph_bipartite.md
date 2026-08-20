# 14. Is Graph Bipartite?

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Depth-First Search, Breadth-First Search, Union Find, Graph

---

## Problem Statement

There is an **undirected** graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to.

A graph is **bipartite** if the nodes can be partitioned into two independent sets `A` and `B` such that every edge in the graph connects a node in set `A` and a node in set `B`.

Return `true` if and only if it is bipartite.

---

## Input & Output Format

- **Input**: An adjacency list `graph`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
```

**Output:**
```text
false
```

**Explanation:**
Contains odd cycles (triangle 0-1-2), cannot be 2-colored.

### Example 2

**Input:**
```text
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
```

**Output:**
```text
true
```

**Explanation:**
Can partition nodes into {0, 2} and {1, 3}.

### Example 3

**Input:**
```text
graph = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8, 1], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]
```

**Output:**
```text
false
```

**Explanation:**
Odd length cycle prevents bipartition.

---

## Constraints

- `graph.length == n`
- `1 <= n <= 100`
- `0 <= graph[u].length < n`
- `0 <= graph[u][i] <= n - 1`
- `graph[u]` does not contain `u` (no self-loops).
- `graph[u]` does not contain duplicate values.

---

## Complexity Analysis

- **Time Complexity**: `O(V + E)`
- **Space Complexity**: `O(V)`
