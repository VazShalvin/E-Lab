# 5. Max Area of Island

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

---

## Problem Statement

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return the maximum **area** of an island in `grid`. If there is no island, return `0`.

---

## Input & Output Format

- **Input**: A 2D binary matrix `grid`.
- **Output**: An integer representing the maximum area.

---

## Sample Test Cases

### Example 1

**Input:**
```text
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
```

**Output:**
```text
6
```

**Explanation:**
The largest connected component of 1s contains 6 cells.

### Example 2

**Input:**
```text
grid = [[0,0,0,0,0,0,0,0]]
```

**Output:**
```text
0
```

**Explanation:**
No islands.

### Example 3

**Input:**
```text
grid = [[1, 1], [1, 0]]
```

**Output:**
```text
3
```

**Explanation:**
Area is 3.

---

## Constraints

- `m == grid.length`, `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1`.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M * N)`
