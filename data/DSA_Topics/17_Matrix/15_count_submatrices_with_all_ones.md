# 15. Count Submatrices With All Ones

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack

---

## Problem Statement

Given an `m x n` binary matrix `mat`, return the number of submatrices that have all ones.

---

## Input & Output Format

- **Input**: A 2D binary matrix `mat`.
- **Output**: An integer representing the total count of all-one submatrices.

---

## Sample Test Cases

### Example 1

**Input:**
```text
mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
```

**Output:**
```text
13
```

**Explanation:**
Submatrices: 1x1: 6, 1x2: 2, 1x3: 0, 2x1: 3, 2x2: 1, 3x1: 1. Total = 13.

### Example 2

**Input:**
```text
mat = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]
```

**Output:**
```text
24
```

**Explanation:**
24 all-one submatrices found.

### Example 3

**Input:**
```text
mat = [[1, 1], [1, 1]]
```

**Output:**
```text
9
```

**Explanation:**
4 (1x1) + 2 (1x2) + 2 (2x1) + 1 (2x2) = 9.

---

## Constraints

- `1 <= m, n <= 150`
- `mat[i][j]` is either `0` or `1`.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(N)`
