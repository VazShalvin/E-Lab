# 4. K Closest Points to Origin

**Topic**: Heap / Priority Queue  
**Difficulty**: Medium  
**Tags**: Array, Math, Divide and Conquer, Geometry, Sorting, Heap, Quickselect

---

## Problem Statement

Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance (i.e., `√(x_1 - x_2)^2 + (y_1 - y_2)^2`).

You may return the answer in any order.

---

## Input & Output Format

- **Input**: A 2D array of points `points` and an integer `k`.
- **Output**: A 2D array of `k` closest points.

---

## Sample Test Cases

### Example 1

**Input:**
```text
points = [[1, 3], [-2, 2]], k = 1
```

**Output:**
```text
[[-2, 2]]
```

**Explanation:**
Distance of (1, 3) = sqrt(10). Distance of (-2, 2) = sqrt(8). Since sqrt(8) < sqrt(10), [-2, 2] is closer.

### Example 2

**Input:**
```text
points = [[3, 3], [5, -1], [-2, 4]], k = 2
```

**Output:**
```text
[[3, 3], [-2, 4]]
```

**Explanation:**
Distances: (3, 3)->18, (-2, 4)->20, (5, -1)->26. Closest two are [[3, 3], [-2, 4]].

### Example 3

**Input:**
```text
points = [[0, 1], [1, 0]], k = 2
```

**Output:**
```text
[[0, 1], [1, 0]]
```

**Explanation:**
Both have distance 1.

---

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 < x_i, y_i < 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N log k)`
- **Space Complexity**: `O(k)`
