# 1. Count Primes (Sieve of Eratosthenes)

**Topic**: Math & Number Theory  
**Difficulty**: Medium  
**Tags**: Array, Math, Number Theory

---

## Problem Statement

Given an integer `n`, return the number of prime numbers that are strictly less than `n` using the **Sieve of Eratosthenes** algorithm.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: An integer representing the count of primes `< n`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 10
```

**Output:**
```text
4
```

**Explanation:**
There are 4 prime numbers less than 10: 2, 3, 5, 7.

### Example 2

**Input:**
```text
n = 0
```

**Output:**
```text
0
```

**Explanation:**
No primes less than 0.

### Example 3

**Input:**
```text
n = 1
```

**Output:**
```text
0
```

**Explanation:**
No primes less than 1.

---

## Constraints

- `0 <= n <= 5 * 10^6`

---

## Complexity Analysis

- **Time Complexity**: `O(N log log N)`
- **Space Complexity**: `O(N)`
