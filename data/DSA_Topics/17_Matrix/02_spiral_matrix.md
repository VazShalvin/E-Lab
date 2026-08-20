# 2. Spiral Matrix

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Matrix, Simulation

---

## Problem Statement

Given an `m x n` matrix, return all elements of the matrix in **spiral order**.

---

## Input & Output Format

- **Input**: A 2D integer matrix `matrix`.
- **Output**: An array of integers in spiral order.

---

## Sample Test Cases

### Example 1

**Input:**
```text
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**Output:**
```text
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

**Explanation:**
Clockwise spiral from top-left.

### Example 2

**Input:**
```text
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```

**Output:**
```text
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

**Explanation:**
Spiral traversal.

### Example 3

**Input:**
```text
matrix = [[1]]
```

**Output:**
```text
[1]
```

**Explanation:**
Single cell.

---

## Constraints

- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(1) extra space`
