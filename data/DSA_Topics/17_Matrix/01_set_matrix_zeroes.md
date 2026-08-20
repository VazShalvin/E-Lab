# 1. Set Matrix Zeroes

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Matrix

---

## Problem Statement

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place with `O(1)` extra space.

---

## Input & Output Format

- **Input**: A 2D array `matrix`.
- **Output**: Modified 2D array in-place.

---

## Sample Test Cases

### Example 1

**Input:**
```text
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
```

**Output:**
```text
[[1, 0, 1], [0, 0, 0], [1, 0, 1]]
```

**Explanation:**
Row 1 and column 1 set to 0.

### Example 2

**Input:**
```text
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
```

**Output:**
```text
[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
```

**Explanation:**
Rows 0 and columns 0, 3 set to 0.

### Example 3

**Input:**
```text
matrix = [[1]]
```

**Output:**
```text
[[1]]
```

**Explanation:**
No zeroes.

---

## Constraints

- `m == matrix.length`, `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(1)`
