# 10. Sqrt(x) using Binary Search

**Topic**: Binary Search  
**Difficulty**: Easy  
**Tags**: Math, Binary Search

---

## Problem Statement

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

---

## Input & Output Format

- **Input**: An integer `x`.
- **Output**: An integer representing `floor(sqrt(x))`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
x = 4
```

**Output:**
```text
2
```

**Explanation:**
The square root of 4 is 2, so we return 2.

### Example 2

**Input:**
```text
x = 8
```

**Output:**
```text
2
```

**Explanation:**
The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

### Example 3

**Input:**
```text
x = 0
```

**Output:**
```text
0
```

**Explanation:**
Square root of 0 is 0.

---

## Constraints

- `0 <= x <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(log x)`
- **Space Complexity**: `O(1)`
