# 14. Prime Factorization & Pollard's Rho Concept

**Topic**: Math & Number Theory  
**Difficulty**: Medium  
**Tags**: Math, Number Theory

---

## Problem Statement

Given a positive integer `N`, find its prime factorization in ascending order, returning each prime factor along with its power/exponent.

For example, `24 = 2^3 * 3^1` should be represented as `[[2, 3], [3, 1]]`.

---

## Input & Output Format

- **Input**: An integer `N`.
- **Output**: A 2D array of pairs `[[prime, power], ...]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
N = 100
```

**Output:**
```text
[[2, 2], [5, 2]]
```

**Explanation:**
100 = 2^2 * 5^2.

### Example 2

**Input:**
```text
N = 37
```

**Output:**
```text
[[37, 1]]
```

**Explanation:**
37 is prime.

### Example 3

**Input:**
```text
N = 360
```

**Output:**
```text
[[2, 3], [3, 2], [5, 1]]
```

**Explanation:**
360 = 2^3 * 3^2 * 5^1.

---

## Constraints

- `2 <= N <= 10^12`

---

## Complexity Analysis

- **Time Complexity**: `O(sqrt(N))`
- **Space Complexity**: `O(log N)`
