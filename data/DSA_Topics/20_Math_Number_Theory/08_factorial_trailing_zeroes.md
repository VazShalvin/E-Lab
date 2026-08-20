# 8. Factorial Trailing Zeroes (Legendre's Formula)

**Topic**: Math & Number Theory  
**Difficulty**: Medium  
**Tags**: Math

---

## Problem Statement

Given an integer `n`, return the number of trailing zeroes in `n!`.

Note that `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`.

Your solution should have `O(log n)` time complexity by counting factors of 5.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: An integer count of trailing zeroes.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 3
```

**Output:**
```text
0
```

**Explanation:**
3! = 6, no trailing zero.

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
1
```

**Explanation:**
5! = 120, one trailing zero.

### Example 3

**Input:**
```text
n = 25
```

**Output:**
```text
6
```

**Explanation:**
floor(25/5) + floor(25/25) = 5 + 1 = 6.

---

## Constraints

- `0 <= n <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(log5 N)`
- **Space Complexity**: `O(1)`
