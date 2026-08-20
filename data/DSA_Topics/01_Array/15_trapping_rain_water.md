# 15. Trapping Rain Water

**Topic**: Array  
**Difficulty**: Hard  
**Tags**: Array, Two Pointers, Dynamic Programming, Stack

---

## Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

---

## Input & Output Format

- **Input**: An array of integers `height`.
- **Output**: An integer representing the total units of trapped water.

---

## Sample Test Cases

### Example 1

**Input:**
```text
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
```

**Output:**
```text
6
```

**Explanation:**
The elevation map [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] traps 6 units of rain water.

### Example 2

**Input:**
```text
height = [4, 2, 0, 3, 2, 5]
```

**Output:**
```text
9
```

**Explanation:**
Trapped water: 0 + 2 + 4 + 1 + 2 + 0 = 9 units.

### Example 3

**Input:**
```text
height = [3, 0, 0, 2, 0, 4]
```

**Output:**
```text
10
```

**Explanation:**
Trapped water: 0 + 3 + 3 + 1 + 3 + 0 = 10 units.

---

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
