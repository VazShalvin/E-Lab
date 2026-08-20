# 12. Network Delay Time (Dijkstra's Algorithm)

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Depth-First Search, Breadth-First Search, Graph, Heap, Shortest Path

---

## Problem Statement

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u_i, v_i, w_i)`, where `u_i` is the source node, `v_i` is the target node, and `w_i` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the **minimum** time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

---

## Input & Output Format

- **Input**: A 2D array `times`, an integer `n`, and an integer `k`.
- **Output**: An integer representing the delay time, or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2
```

**Output:**
```text
2
```

**Explanation:**
Signal from 2 reaches 1 and 3 in 1 time unit, and reaches 4 via 3 at time 2. Max time across all nodes is 2.

### Example 2

**Input:**
```text
times = [[1, 2, 1]], n = 2, k = 1
```

**Output:**
```text
1
```

**Explanation:**
Reaches node 2 in 1 unit.

### Example 3

**Input:**
```text
times = [[1, 2, 1]], n = 2, k = 2
```

**Output:**
```text
-1
```

**Explanation:**
Cannot reach node 1 from node 2.

---

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= u_i, v_i <= n`
- `1 <= w_i <= 100`
- All pairs `(u_i, v_i)` are unique.

---

## Complexity Analysis

- **Time Complexity**: `O(E log V)`
- **Space Complexity**: `O(V + E)`
