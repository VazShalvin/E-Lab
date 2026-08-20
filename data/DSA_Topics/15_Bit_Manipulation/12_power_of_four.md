# 12. Power of Four

**Topic**: Bit Manipulation  
**Difficulty**: Easy  
**Tags**: Math, Bit Manipulation, Recursion

---

## Problem Statement

Given an integer `n`, return `true` if it is a power of four. Otherwise, return `false`.

An integer `n` is a power of four, if there exists an integer `x` such that `n == 4^x`.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 16
```

**Output:**
```text
true
```

**Explanation:**
4^2 = 16.

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
false
```

**Explanation:**
5 is not a power of 4.

### Example 3

**Input:**
```text
n = 1
```

**Output:**
```text
true
```

**Explanation:**
4^0 = 1.

---

## Constraints

- `-2^31 <= n <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`
