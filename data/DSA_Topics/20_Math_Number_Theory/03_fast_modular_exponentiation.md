# 3. Fast Modular Exponentiation

**Topic**: Math & Number Theory  
**Difficulty**: Medium  
**Tags**: Math, Number Theory, Divide and Conquer

---

## Problem Statement

Given three integers `base`, `exp`, and `mod`, compute `(base^exp) % mod` efficiently in `O(log exp)` time without integer overflow.

---

## Input & Output Format

- **Input**: Three integers `base`, `exp`, and `mod`.
- **Output**: An integer representing `(base^exp) % mod`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
base = 2, exp = 10, mod = 1000
```

**Output:**
```text
24
```

**Explanation:**
2^10 = 1024. 1024 % 1000 = 24.

### Example 2

**Input:**
```text
base = 3, exp = 13, mod = 7
```

**Output:**
```text
3
```

**Explanation:**
(3^13) % 7 = 3.

### Example 3

**Input:**
```text
base = 5, exp = 0, mod = 13
```

**Output:**
```text
1
```

**Explanation:**
5^0 % 13 = 1.

---

## Constraints

- `0 <= base <= 10^9`
- `0 <= exp <= 10^9`
- `1 <= mod <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(log exp)`
- **Space Complexity**: `O(1)`
