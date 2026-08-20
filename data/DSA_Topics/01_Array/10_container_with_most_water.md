# 10. Container With Most Water

**Topic**: Array  
**Difficulty**: Medium  
**Tags**: Array, Two Pointers, Greedy

---

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

---

## Input & Output Format

- **Input**: An array of integers `height`.
- **Output**: An integer representing the maximum area.

---

## Sample Test Cases

### Example 1

**Input:**
```text
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```

**Output:**
```text
49
```

**Explanation:**
The vertical lines are at indices [1, 8, 6, 2, 5, 4, 8, 3, 7]. The max area is between index 1 (height 8) and index 8 (height 7): min(8, 7) * (8 - 1) = 7 * 7 = 49.

### Example 2

**Input:**
```text
height = [1, 1]
```

**Output:**
```text
1
```

**Explanation:**
min(1, 1) * (1 - 0) = 1.

### Example 3

**Input:**
```text
height = [4, 3, 2, 1, 4]
```

**Output:**
```text
16
```

**Explanation:**
Between index 0 (height 4) and index 4 (height 4): min(4, 4) * (4 - 0) = 16.

---

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
