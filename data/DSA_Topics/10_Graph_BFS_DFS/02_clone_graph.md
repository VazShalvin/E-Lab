# 2. Clone Graph

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Hash Table, Depth-First Search, Breadth-First Search, Graph

---

## Problem Statement

Given a reference of a node in a **connected** undirected graph.

Return a **deep copy** (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

---

## Input & Output Format

- **Input**: An adjacency list representation of a connected undirected graph.
- **Output**: A deep cloned graph root node.

---

## Sample Test Cases

### Example 1

**Input:**
```text
adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
```

**Output:**
```text
[[2, 4], [1, 3], [2, 4], [1, 3]]
```

**Explanation:**
Node 1 connects to 2,4; Node 2 connects to 1,3; Node 3 connects to 2,4; Node 4 connects to 1,3. All cloned into new node objects.

### Example 2

**Input:**
```text
adjList = [[]]
```

**Output:**
```text
[[]]
```

**Explanation:**
Single node with no neighbors.

### Example 3

**Input:**
```text
adjList = []
```

**Output:**
```text
[]
```

**Explanation:**
Empty graph returns null/empty.

---

## Constraints

- The number of nodes in the graph is in the range `[0, 100]`.
- `1 <= Node.val <= 100`
- `Node.val` is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

---

## Complexity Analysis

- **Time Complexity**: `O(V + E)`
- **Space Complexity**: `O(V)`
