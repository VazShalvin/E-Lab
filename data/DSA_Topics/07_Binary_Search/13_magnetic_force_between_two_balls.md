# 13. Magnetic Force Between Two Balls (Aggressive Cows)

**Topic**: Binary Search  
**Difficulty**: Medium  
**Tags**: Array, Binary Search, Sorting

---

## Problem Statement

In the universe, there are `n` empty baskets, each placed at `position[i]`. We have `m` balls and want to distribute the balls into the baskets such that the **minimum magnetic force** between any two balls is **maximum**.

The magnetic force between two different balls at positions `x` and `y` is `|x - y|`.

Given the integer array `position` and the integer `m`, return the required maximum minimum magnetic force.

---

## Input & Output Format

- **Input**: An array of integers `position` and an integer `m`.
- **Output**: An integer representing the maximized minimum distance.

---

## Sample Test Cases

### Example 1

**Input:**
```text
position = [1, 2, 3, 4, 7], m = 3
```

**Output:**
```text
3
```

**Explanation:**
Distributing 3 balls into baskets 1, 4, 7 gives minimum force of 3.

### Example 2

**Input:**
```text
position = [5, 4, 3, 2, 1, 1000000000], m = 2
```

**Output:**
```text
999999999
```

**Explanation:**
Distribute 2 balls at positions 1 and 1000000000.

### Example 3

**Input:**
```text
position = [1, 2], m = 2
```

**Output:**
```text
1
```

**Explanation:**
Distance between 1 and 2 is 1.

---

## Constraints

- `n == position.length`
- `2 <= n <= 10^5`
- `1 <= position[i] <= 10^9`
- All integers in `position` are distinct.
- `2 <= m <= position.length`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N + N log(max_pos))`
- **Space Complexity**: `O(1)`
