# 14. Divide Two Integers (Bit Shift Division)

**Topic**: Bit Manipulation  
**Difficulty**: Medium  
**Tags**: Math, Bit Manipulation

---

## Problem Statement

Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero. Return the quotient after dividing `dividend` by `divisor`.

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: `[-2^31, 2^31 - 1]`. If quotient exceeds range, clamp to bound.

---

## Input & Output Format

- **Input**: Two integers `dividend` and `divisor`.
- **Output**: An integer representing the quotient.

---

## Sample Test Cases

### Example 1

**Input:**
```text
dividend = 10, divisor = 3
```

**Output:**
```text
3
```

**Explanation:**
10/3 = 3.33333.. which is truncated to 3.

### Example 2

**Input:**
```text
dividend = 7, divisor = -3
```

**Output:**
```text
-2
```

**Explanation:**
7/-3 = -2.33333.. which is truncated to -2.

### Example 3

**Input:**
```text
dividend = -2147483648, divisor = -1
```

**Output:**
```text
2147483647
```

**Explanation:**
Clamped to INT_MAX (2^31 - 1).

---

## Constraints

- `-2^31 <= dividend, divisor <= 2^31 - 1`
- `divisor != 0`

---

## Complexity Analysis

- **Time Complexity**: `O(log^2 N) or O(32)`
- **Space Complexity**: `O(1)`
