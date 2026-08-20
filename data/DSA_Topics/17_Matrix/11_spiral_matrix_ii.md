# 11. Spiral Matrix II (Generate N x N)

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Matrix, Simulation

---

## Problem Statement

Given a positive integer `n`, generate an `n x n` `matrix` filled with elements from `1` to `n^2` in spiral order.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: A 2D array of integers of dimension `n x n`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 3
```

**Output:**
```text
[[1, 2, 3], [8, 9, 4], [7, 6, 5]]
```

**Explanation:**
Numbers 1 to 9 placed in clockwise spiral.

### Example 2

**Input:**
```text
n = 1
```

**Output:**
```text
[[1]]
```

**Explanation:**
1x1 matrix.

### Example 3

**Input:**
```text
n = 2
```

**Output:**
```text
[[1, 2], [4, 3]]
```

**Explanation:**
2x2 spiral.

---

## Constraints

- `1 <= n <= 20`

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(1) auxiliary`
