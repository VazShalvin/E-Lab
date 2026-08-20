# 7. Minimum Number of Arrows to Burst Balloons

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: Array, Greedy, Sorting

---

## Problem Statement

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [x_start, x_end]` denotes a balloon whose horizontal diameter stretches between `x_start` and `x_end`.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with `x_start` and `x_end` is burst by an arrow shot at `x` if `x_start <= x <= x_end`.

Given the array `points`, return the **minimum number of arrows** that must be shot to burst all balloons.

---

## Input & Output Format

- **Input**: A 2D array `points`.
- **Output**: An integer representing the minimum arrows.

---

## Sample Test Cases

### Example 1

**Input:**
```text
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
```

**Output:**
```text
2
```

**Explanation:**
The balloons can be burst by 2 arrows: shoot at x = 6 (bursting [2, 8] and [1, 6]) and x = 11 (bursting [10, 16] and [7, 12]).

### Example 2

**Input:**
```text
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
```

**Output:**
```text
4
```

**Explanation:**
One arrow per balloon needed.

### Example 3

**Input:**
```text
points = [[1, 2], [2, 3], [3, 4], [4, 5]]
```

**Output:**
```text
2
```

**Explanation:**
Shoot at x = 2 and x = 4.

---

## Constraints

- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `-2^31 <= x_start < x_end <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(1)`
