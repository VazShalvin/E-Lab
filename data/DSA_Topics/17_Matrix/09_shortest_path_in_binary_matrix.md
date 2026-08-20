# 9. Shortest Path in Binary Matrix

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Breadth-First Search, Matrix

---

## Problem Statement

Given an `n x n` binary matrix `grid`, return the length of the shortest **clear path** in the matrix. If there is no clear path, return `-1`.

A clear path in a binary matrix is a path from the **top-left cell** (i.e., `(0, 0)`) to the **bottom-right cell** (i.e., `(n - 1, n - 1)`) such that:
- All the visited cells of the path are `0`.
- All the adjacent cells of the path are **8-directionally connected**.

The length of a clear path is the number of visited cells of this path.

---

## Input & Output Format

- **Input**: A 2D binary matrix `grid`.
- **Output**: An integer representing shortest path length or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
grid = [[0, 1], [1, 0]]
```

**Output:**
```text
2
```

**Explanation:**
(0,0) -> (1,1) diagonal step of length 2.

### Example 2

**Input:**
```text
grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
```

**Output:**
```text
4
```

**Explanation:**
(0,0) -> (0,1) -> (1,2) -> (2,2) length 4.

### Example 3

**Input:**
```text
grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
```

**Output:**
```text
-1
```

**Explanation:**
Start cell is 1, no clear path.

---

## Constraints

- `n == grid.length == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` is `0` or `1`.

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`
