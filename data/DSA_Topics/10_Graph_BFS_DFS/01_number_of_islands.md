# 1. Number of Islands

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

---

## Problem Statement

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

---

## Input & Output Format

- **Input**: A 2D character matrix `grid`.
- **Output**: An integer representing the number of islands.

---

## Sample Test Cases

### Example 1

**Input:**
```text
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
```

**Output:**
```text
1
```

**Explanation:**
All connected 1s form one large island.

### Example 2

**Input:**
```text
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
```

**Output:**
```text
3
```

**Explanation:**
Three disjoint islands.

### Example 3

**Input:**
```text
grid = [["0","0"],["0","0"]]
```

**Output:**
```text
0
```

**Explanation:**
No islands.

---

## Constraints

- `m == grid.length`, `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M * N)`
