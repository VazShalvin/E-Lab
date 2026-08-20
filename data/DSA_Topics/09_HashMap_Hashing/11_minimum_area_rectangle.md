# 11. Minimum Area Rectangle

**Topic**: HashMap / Hashing  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Math, Geometry, Sorting

---

## Problem Statement

You are given an array of points in the X-Y plane `points` where `points[i] = [x_i, y_i]`.

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return `0`.

---

## Input & Output Format

- **Input**: A 2D array of points `points`.
- **Output**: An integer representing the minimum area (or 0).

---

## Sample Test Cases

### Example 1

**Input:**
```text
points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
```

**Output:**
```text
4
```

**Explanation:**
Rectangle formed by [1, 1], [1, 3], [3, 1], [3, 3] has area |3-1| * |3-1| = 4.

### Example 2

**Input:**
```text
points = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
```

**Output:**
```text
2
```

**Explanation:**
Rectangle formed by [3, 1], [3, 3], [4, 1], [4, 3] has area 2.

### Example 3

**Input:**
```text
points = [[1, 1], [2, 2], [3, 3]]
```

**Output:**
```text
0
```

**Explanation:**
No rectangle parallel to axes can be formed.

---

## Constraints

- `1 <= points.length <= 500`
- `points[i].length == 2`
- `0 <= x_i, y_i <= 4 * 10^4`
- All given points are **unique**.

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`
