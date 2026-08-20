# 10. Car Fleet

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, Stack, Sorting, Monotonic Stack

---

## Problem Statement

There are `n` cars at given miles away from the starting mile 0, traveling to reach the destination at mile `target`.

You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting position of the `i-th` car and `speed[i]` is the speed of the `i-th` car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. A **car fleet** is some non-empty set of cars driving at the same position and same speed.

Return the **number of car fleets** that will arrive at the destination.

---

## Input & Output Format

- **Input**: An integer `target`, and arrays `position` and `speed`.
- **Output**: An integer count of car fleets.

---

## Sample Test Cases

### Example 1

**Input:**
```text
target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
```

**Output:**
```text
3
```

**Explanation:**
The cars starting at 10 and 8 form a fleet at mile 12. The cars starting at 5 and 3 form a fleet at mile 6. The car starting at 0 never catches up. Total 3 fleets.

### Example 2

**Input:**
```text
target = 10, position = [3], speed = [3]
```

**Output:**
```text
1
```

**Explanation:**
Only 1 car, so 1 fleet.

### Example 3

**Input:**
```text
target = 100, position = [0, 2, 4], speed = [4, 2, 1]
```

**Output:**
```text
1
```

**Explanation:**
All cars merge into 1 fleet.

---

## Constraints

- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`
- `0 <= position[i] < target`
- All the values of `position` are **unique**.
- `0 < speed[i] <= 10^6`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
