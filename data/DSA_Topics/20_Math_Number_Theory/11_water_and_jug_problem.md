# 11. Water and Jug Problem (Bézout's Identity)

**Topic**: Math & Number Theory  
**Difficulty**: Medium  
**Tags**: Math, Depth-First Search, Breadth-First Search

---

## Problem Statement

You are given two jugs with capacities `x` and `y` liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly `target` liters using these two jugs.

If `target` liters of water is measurable, you must have `target` liters of water contained within one or both buckets by the end.

Operations allowed:
- Fill any jug completely with water.
- Empty any jug.
- Pour water from one jug into another until the other jug is completely full, or the first jug itself is empty.

---

## Input & Output Format

- **Input**: Three integers `x`, `y`, and `target`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
x = 3, y = 5, target = 4
```

**Output:**
```text
true
```

**Explanation:**
gcd(3, 5) = 1, 4 is divisible by 1 and <= 3 + 5 = 8.

### Example 2

**Input:**
```text
x = 2, y = 6, target = 5
```

**Output:**
```text
false
```

**Explanation:**
gcd(2, 6) = 2, 5 is odd so not divisible by 2.

### Example 3

**Input:**
```text
x = 1, y = 2, target = 3
```

**Output:**
```text
true
```

**Explanation:**
1 + 2 = 3.

---

## Constraints

- `1 <= x, y, target <= 10^6`

---

## Complexity Analysis

- **Time Complexity**: `O(log(min(x, y)))`
- **Space Complexity**: `O(1)`
