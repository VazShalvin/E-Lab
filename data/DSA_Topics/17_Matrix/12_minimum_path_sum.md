# 12. Minimum Path Sum in Grid

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Matrix

---

## Problem Statement

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

---

## Input & Output Format

- **Input**: A 2D integer matrix `grid`.
- **Output**: An integer representing the minimum path sum.

---

## Sample Test Cases

### Example 1

**Input:**
```text
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
```

**Output:**
```text
7
```

**Explanation:**
Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum (1 + 3 + 1 + 1 + 1 = 7).

### Example 2

**Input:**
```text
grid = [[1, 2, 3], [4, 5, 6]]
```

**Output:**
```text
12
```

**Explanation:**
Path 1 -> 2 -> 3 -> 6 = 12.

### Example 3

**Input:**
```text
grid = [[5]]
```

**Output:**
```text
5
```

**Explanation:**
Single cell.

---

## Constraints

- `m == grid.length`, `n == grid[0].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(N) or O(1) in-place`
