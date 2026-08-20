# 7. Minimum Cost to Connect Sticks

**Topic**: Heap / Priority Queue  
**Difficulty**: Medium  
**Tags**: Array, Greedy, Heap

---

## Problem Statement

You have some number of sticks with positive integer lengths. These lengths are given as an array `sticks`, where `sticks[i]` is the length of the `i-th` stick.

You can connect any two sticks of lengths `x` and `y` into one stick by paying a cost of `x + y`. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks in this way.

---

## Input & Output Format

- **Input**: An array of integers `sticks`.
- **Output**: An integer representing the minimum cost.

---

## Sample Test Cases

### Example 1

**Input:**
```text
sticks = [2, 4, 3]
```

**Output:**
```text
14
```

**Explanation:**
1. Connect sticks 2 and 3 for cost 5 -> [4, 5]
2. Connect sticks 4 and 5 for cost 9 -> [9]
Total cost = 5 + 9 = 14.

### Example 2

**Input:**
```text
sticks = [1, 8, 3, 5]
```

**Output:**
```text
30
```

**Explanation:**
Connect 1 and 3 (cost 4), then 4 and 5 (cost 9), then 8 and 9 (cost 17). Total = 4 + 9 + 17 = 30.

### Example 3

**Input:**
```text
sticks = [5]
```

**Output:**
```text
0
```

**Explanation:**
Only one stick, 0 cost.

---

## Constraints

- `1 <= sticks.length <= 10^4`
- `1 <= sticks[i] <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
