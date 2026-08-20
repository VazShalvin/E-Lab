# 3. Rotate Image (90 Degrees In-Place)

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Math, Matrix

---

## Problem Statement

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90 degrees (clockwise)** in-place.

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix for the rotation.

---

## Input & Output Format

- **Input**: A 2D array `matrix`.
- **Output**: Matrix rotated 90 degrees clockwise in-place.

---

## Sample Test Cases

### Example 1

**Input:**
```text
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**Output:**
```text
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

**Explanation:**
Transpose matrix + reverse each row.

### Example 2

**Input:**
```text
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
```

**Output:**
```text
[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
```

**Explanation:**
90 degree clockwise rotation.

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
1x1 matrix unchanged.

---

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(1)`
