# 1. Fibonacci Number & Matrix Exponentiation

**Topic**: Recursion  
**Difficulty**: Easy  
**Tags**: Math, Dynamic Programming, Recursion, Matrix Exponentiation

---

## Problem Statement

The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`.

Given `n`, calculate `F(n)` using recursion, memoization, or `O(log n)` Matrix Exponentiation.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: An integer representing `F(n)`.

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
F(2) = F(1) + F(0) = 1 + 0 = 1.

### Example 2

**Input:**
```text
n = 3
```

**Output:**
```text
2
```

**Explanation:**
F(3) = F(2) + F(1) = 1 + 1 = 2.

### Example 3

**Input:**
```text
n = 4
```

**Output:**
```text
3
```

**Explanation:**
F(4) = F(3) + F(2) = 2 + 1 = 3.

---

## Constraints

- `0 <= n <= 30`

---

## Complexity Analysis

- **Time Complexity**: `O(N) with memoization or O(log N) matrix exponentiation`
- **Space Complexity**: `O(N)`
