# 11. Power of Two

**Topic**: Bit Manipulation  
**Difficulty**: Easy  
**Tags**: Math, Bit Manipulation, Recursion

---

## Problem Statement

Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2^x`.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 1
```

**Output:**
```text
true
```

**Explanation:**
2^0 = 1.

### Example 2

**Input:**
```text
n = 16
```

**Output:**
```text
true
```

**Explanation:**
2^4 = 16 (in binary: 10000, n & (n - 1) == 0).

### Example 3

**Input:**
```text
n = 3
```

**Output:**
```text
false
```

**Explanation:**
3 is not a power of two.

---

## Constraints

- `-2^31 <= n <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`
