# 11. Redundant Connection

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Depth-First Search, Breadth-First Search, Union Find, Graph

---

## Problem Statement

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [a_i, b_i]`.

Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.

---

## Input & Output Format

- **Input**: A 2D array `edges`.
- **Output**: An array of two integers `[u, v]` representing the redundant edge.

---

## Sample Test Cases

### Example 1

**Input:**
```text
edges = [[1, 2], [1, 3], [2, 3]]
```

**Output:**
```text
[2, 3]
```

**Explanation:**
Removing [2, 3] leaves a valid tree connected by [1, 2] and [1, 3].

### Example 2

**Input:**
```text
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
```

**Output:**
```text
[1, 4]
```

**Explanation:**
Cycle formed by [1, 2, 3, 4], [1, 4] is the latest occurring edge.

### Example 3

**Input:**
```text
edges = [[1, 2], [2, 3], [1, 3]]
```

**Output:**
```text
[1, 3]
```

**Explanation:**
Edge [1, 3] creates cycle.

---

## Constraints

- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= a_i < b_i <= n`
- `a_i != b_i`
- There are no repeated edges.

---

## Complexity Analysis

- **Time Complexity**: `O(N * α(N)) using Union-Find`
- **Space Complexity**: `O(N)`
