# 13. Cheapest Flights Within K Stops (Bellman-Ford / BFS)

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Dynamic Programming, Depth-First Search, Breadth-First Search, Graph, Heap, Shortest Path

---

## Problem Statement

There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`, return the **cheapest price** from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

---

## Input & Output Format

- **Input**: An integer `n`, 2D array `flights`, and integers `src`, `dst`, `k`.
- **Output**: An integer representing cheapest price or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 4, flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src = 0, dst = 3, k = 1
```

**Output:**
```text
700
```

**Explanation:**
The path 0 -> 1 -> 3 has cost 100 + 600 = 700 with 1 stop.

### Example 2

**Input:**
```text
n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 1
```

**Output:**
```text
200
```

**Explanation:**
The path 0 -> 1 -> 2 has cost 100 + 100 = 200 with 1 stop.

### Example 3

**Input:**
```text
n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 0
```

**Output:**
```text
500
```

**Explanation:**
With 0 stops, direct flight cost is 500.

---

## Constraints

- `1 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= from_i, to_i < n`
- `from_i != to_i`
- `1 <= price_i <= 10^4`
- `0 <= src, dst, k < n`
- `src != dst`

---

## Complexity Analysis

- **Time Complexity**: `O(k * E)`
- **Space Complexity**: `O(V)`
