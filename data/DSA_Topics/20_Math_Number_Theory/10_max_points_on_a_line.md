# 10. Max Points on a Line

**Topic**: Math & Number Theory  
**Difficulty**: Hard  
**Tags**: Array, Hash Table, Math, Geometry

---

## Problem Statement

Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on the **X-Y** plane, return the maximum number of points that lie on the same straight line.

---

## Input & Output Format

- **Input**: A 2D array `points`.
- **Output**: An integer representing maximum collinear points.

---

## Sample Test Cases

### Example 1

**Input:**
```text
points = [[1, 1], [2, 2], [3, 3]]
```

**Output:**
```text
3
```

**Explanation:**
All 3 points lie on the line y = x.

### Example 2

**Input:**
```text
points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
```

**Output:**
```text
4
```

**Explanation:**
Points [1, 4], [2, 3], [3, 2], [4, 1] lie on line x + y = 5.

### Example 3

**Input:**
```text
points = [[1, 1]]
```

**Output:**
```text
1
```

**Explanation:**
Single point.

---

## Constraints

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-10^4 <= x_i, y_i <= 10^4`
- All the `points` are **unique**.

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`
