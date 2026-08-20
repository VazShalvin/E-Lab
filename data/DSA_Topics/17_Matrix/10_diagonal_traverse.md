# 10. Diagonal Traverse

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Matrix, Simulation

---

## Problem Statement

Given an `m x n` matrix `mat`, return an array of all the elements of the array in a diagonal order (alternating upward and downward diagonals).

---

## Input & Output Format

- **Input**: A 2D integer matrix `mat`.
- **Output**: An array of integers traversed diagonally.

---

## Sample Test Cases

### Example 1

**Input:**
```text
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**Output:**
```text
[1, 2, 4, 7, 5, 3, 6, 8, 9]
```

**Explanation:**
Alternating diagonals: [1], [2, 4], [7, 5, 3], [6, 8], [9].

### Example 2

**Input:**
```text
mat = [[1, 2], [3, 4]]
```

**Output:**
```text
[1, 2, 3, 4]
```

**Explanation:**
Traversed diagonally.

### Example 3

**Input:**
```text
mat = [[7]]
```

**Output:**
```text
[7]
```

**Explanation:**
Single cell.

---

## Constraints

- `m == mat.length`, `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `-10^5 <= mat[i][j] <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(1) extra space`
