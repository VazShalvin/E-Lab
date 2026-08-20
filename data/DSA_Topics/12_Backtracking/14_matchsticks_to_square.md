# 14. Matchsticks to Square

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask

---

## Problem Statement

You are given an integer array `matchsticks` where `matchsticks[i]` is the length of the `i-th` matchstick. You want to use **all the matchsticks** to make one square. You **should not break** any stick, but you can link them up, and each matchstick must be used **exactly one time**.

Return `true` if you can make this square and `false` otherwise.

---

## Input & Output Format

- **Input**: An array of integers `matchsticks`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
matchsticks = [1, 1, 2, 2, 2]
```

**Output:**
```text
true
```

**Explanation:**
Can form a square of side length 2: (1+1, 2, 2, 2).

### Example 2

**Input:**
```text
matchsticks = [3, 3, 3, 3, 4]
```

**Output:**
```text
false
```

**Explanation:**
Total perimeter is 16, but stick of length 4 cannot be partitioned into 4 equal sides of length 4 with other sticks.

### Example 3

**Input:**
```text
matchsticks = [5, 5, 5, 5]
```

**Output:**
```text
true
```

**Explanation:**
Four sticks of length 5 form square.

---

## Constraints

- `1 <= matchsticks.length <= 15`
- `1 <= matchsticks[i] <= 10^8`

---

## Complexity Analysis

- **Time Complexity**: `O(4^N)`
- **Space Complexity**: `O(N)`
