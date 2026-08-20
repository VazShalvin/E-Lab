# 7. 01 Matrix (Distance to Nearest 0)

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Breadth-First Search, Matrix

---

## Problem Statement

Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell.

The distance between two adjacent cells is `1`.

---

## Input & Output Format

- **Input**: A 2D binary matrix `mat`.
- **Output**: A 2D matrix of integers representing shortest distances to 0.

---

## Sample Test Cases

### Example 1

**Input:**
```text
mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
```

**Output:**
```text
[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
```

**Explanation:**
Distance to nearest 0 for the middle cell is 1.

### Example 2

**Input:**
```text
mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
```

**Output:**
```text
[[0, 0, 0], [0, 1, 0], [1, 2, 1]]
```

**Explanation:**
Multi-source BFS computes shortest distance from 0 cells.

### Example 3

**Input:**
```text
mat = [[0]]
```

**Output:**
```text
[[0]]
```

**Explanation:**
Distance is 0.

---

## Constraints

- `m == mat.length`, `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `mat[i][j]` is either `0` or `1`.
- There is at least one `0` in `mat`.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M * N)`
