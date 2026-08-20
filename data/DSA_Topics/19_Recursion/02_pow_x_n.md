# 2. Pow(x, n) (Fast Exponentiation by Squaring)

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: Math, Recursion

---

## Problem Statement

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`) using recursive divide and conquer.

---

## Input & Output Format

- **Input**: A double `x` and an integer `n`.
- **Output**: A double representing `x^n`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
x = 2.00000, n = 10
```

**Output:**
```text
1024.00000
```

**Explanation:**
2^10 = 1024.

### Example 2

**Input:**
```text
x = 2.10000, n = 3
```

**Output:**
```text
9.26100
```

**Explanation:**
2.1^3 = 9.261.

### Example 3

**Input:**
```text
x = 2.00000, n = -2
```

**Output:**
```text
0.25000
```

**Explanation:**
2^(-2) = 1/(2^2) = 1/4 = 0.25.

---

## Constraints

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- `n` is an integer.
- Either `x` is not zero or `n > 0`.

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(log N) recursion stack`
