# 8. Largest Rectangle in Histogram

**Topic**: Stack  
**Difficulty**: Hard  
**Tags**: Array, Stack, Monotonic Stack

---

## Problem Statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

---

## Input & Output Format

- **Input**: An array of integers `heights`.
- **Output**: An integer representing the largest rectangle area.

---

## Sample Test Cases

### Example 1

**Input:**
```text
heights = [2, 1, 5, 6, 2, 3]
```

**Output:**
```text
10
```

**Explanation:**
The largest rectangle is formed by bars [5, 6] with height 5 and width 2, area = 5 * 2 = 10.

### Example 2

**Input:**
```text
heights = [2, 4]
```

**Output:**
```text
4
```

**Explanation:**
Max area is 4 (bar of height 4 width 1 or height 2 width 2).

### Example 3

**Input:**
```text
heights = [6, 2, 5, 4, 5, 1, 6]
```

**Output:**
```text
12
```

**Explanation:**
Bars [5, 4, 5] with height 4 and width 3 give area = 12.

---

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
