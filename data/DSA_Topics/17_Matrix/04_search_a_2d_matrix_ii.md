# 4. Search a 2D Matrix II

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Binary Search, Divide and Conquer, Matrix

---

## Problem Statement

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

---

## Input & Output Format

- **Input**: A 2D matrix `matrix` and an integer `target`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target = 5
```

**Output:**
```text
true
```

**Explanation:**
5 is present at matrix[1][1].

### Example 2

**Input:**
```text
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target = 20
```

**Output:**
```text
false
```

**Explanation:**
20 does not exist in the matrix.

### Example 3

**Input:**
```text
matrix = [[-5]], target = -5
```

**Output:**
```text
true
```

**Explanation:**
-5 found.

---

## Constraints

- `m == matrix.length`, `n == matrix[i].length`
- `1 <= n, m <= 300`
- `-10^9 <= matrix[i][j], target <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(M + N)`
- **Space Complexity**: `O(1)`
