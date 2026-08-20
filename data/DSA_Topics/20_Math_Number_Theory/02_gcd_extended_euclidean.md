# 2. Greatest Common Divisor & Extended Euclidean Algorithm

**Topic**: Math & Number Theory  
**Difficulty**: Easy  
**Tags**: Math, Number Theory, Recursion

---

## Problem Statement

Given two integers `a` and `b`, calculate their Greatest Common Divisor `gcd(a, b)` and find integers `x` and `y` such that `a * x + b * y = gcd(a, b)` using the **Extended Euclidean Algorithm**.

---

## Input & Output Format

- **Input**: Two integers `a` and `b`.
- **Output**: An integer array `[gcd, x, y]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
a = 35, b = 15
```

**Output:**
```text
gcd: 5, x: 1, y: -2
```

**Explanation:**
35*(1) + 15*(-2) = 35 - 30 = 5 = gcd(35, 15).

### Example 2

**Input:**
```text
a = 10, b = 0
```

**Output:**
```text
gcd: 10, x: 1, y: 0
```

**Explanation:**
10*(1) + 0*(0) = 10.

### Example 3

**Input:**
```text
a = 31, b = 2
```

**Output:**
```text
gcd: 1, x: 1, y: -15
```

**Explanation:**
31*1 + 2*(-15) = 1.

---

## Constraints

- `0 <= a, b <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(log(min(a, b)))`
- **Space Complexity**: `O(log(min(a, b)))`
