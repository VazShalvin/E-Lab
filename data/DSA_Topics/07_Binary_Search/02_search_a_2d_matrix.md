# 2. Search a 2D Matrix

**Topic**: Binary Search  
**Difficulty**: Medium  
**Tags**: Array, Binary Search, Matrix

---

## Problem Statement

You are given an `m x n` integer matrix `matrix` with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.

---

## Input & Output Format

- **Input**: A 2D matrix `matrix` and an integer `target`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
```

**Output:**
```text
true
```

**Explanation:**
3 is located in the first row.

### Example 2

**Input:**
```text
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13
```

**Output:**
```text
false
```

**Explanation:**
13 does not exist in the matrix.

### Example 3

**Input:**
```text
matrix = [[1]], target = 1
```

**Output:**
```text
true
```

**Explanation:**
1 is found.

---

## Constraints

- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(log(M * N))`
- **Space Complexity**: `O(1)`
