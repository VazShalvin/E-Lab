# 6. Flood Fill

**Topic**: Matrix  
**Difficulty**: Easy  
**Tags**: Array, Depth-First Search, Breadth-First Search, Matrix

---

## Problem Statement

An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.

You are also given three integers `sr`, `sc`, and `color`. You should perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `color`.

Return the modified image after performing the flood fill.

---

## Input & Output Format

- **Input**: A 2D array `image`, integers `sr`, `sc`, and `color`.
- **Output**: The modified 2D array.

---

## Sample Test Cases

### Example 1

**Input:**
```text
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2
```

**Output:**
```text
[[2, 2, 2], [2, 2, 0], [2, 0, 1]]
```

**Explanation:**
From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel are colored with the new color.

### Example 2

**Input:**
```text
image = [[0, 0, 0], [0, 0, 0]], sr = 0, sc = 0, color = 0
```

**Output:**
```text
[[0, 0, 0], [0, 0, 0]]
```

**Explanation:**
The starting pixel is already colored 0, so no changes are made.

### Example 3

**Input:**
```text
image = [[1]], sr = 0, sc = 0, color = 5
```

**Output:**
```text
[[5]]
```

**Explanation:**
Single pixel colored 5.

---

## Constraints

- `m == image.length`, `n == image[i].length`
- `1 <= m, n <= 50`
- `0 <= image[i][j], color < 2^16`
- `0 <= sr < m`, `0 <= sc < n`

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M * N)`
