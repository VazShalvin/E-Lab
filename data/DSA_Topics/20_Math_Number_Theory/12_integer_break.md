# 12. Integer Break (Maximize Product)

**Topic**: Math & Number Theory  
**Difficulty**: Medium  
**Tags**: Math, Dynamic Programming

---

## Problem Statement

Given an integer `n`, break it into the sum of `k` **positive integers**, where `k >= 2`, and maximize the product of those integers.

Return the maximum product you can get.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: An integer representing the maximum product.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 2
```

**Output:**
```text
1
```

**Explanation:**
2 = 1 + 1, 1 * 1 = 1.

### Example 2

**Input:**
```text
n = 10
```

**Output:**
```text
36
```

**Explanation:**
10 = 3 + 3 + 4, 3 * 3 * 4 = 36.

### Example 3

**Input:**
```text
n = 6
```

**Output:**
```text
9
```

**Explanation:**
6 = 3 + 3, 3 * 3 = 9.

---

## Constraints

- `2 <= n <= 58`

---

## Complexity Analysis

- **Time Complexity**: `O(log N) math or O(N^2) DP`
- **Space Complexity**: `O(1)`
