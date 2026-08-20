# 9. Rotting Oranges

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Array, Breadth-First Search, Matrix

---

## Problem Statement

You are given an `m x n` grid where each cell can have one of three values:
- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

---

## Input & Output Format

- **Input**: A 2D integer matrix `grid`.
- **Output**: An integer representing minutes elapsed, or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
```

**Output:**
```text
4
```

**Explanation:**
Minute 0: [2, 1, 1]... minute 4 all reachable oranges are rotten.

### Example 2

**Input:**
```text
grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
```

**Output:**
```text
-1
```

**Explanation:**
The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

### Example 3

**Input:**
```text
grid = [[0, 2]]
```

**Output:**
```text
0
```

**Explanation:**
Since there are already no fresh oranges at minute 0, the answer is just 0.

---

## Constraints

- `m == grid.length`, `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M * N)`
