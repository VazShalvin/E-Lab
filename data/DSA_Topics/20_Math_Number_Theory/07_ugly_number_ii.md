# 7. Ugly Number II (Three Pointers DP)

**Topic**: Math & Number Theory  
**Difficulty**: Medium  
**Tags**: Hash Table, Math, Dynamic Programming, Heap

---

## Problem Statement

An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`.

Given an integer `n`, return the `n-th` **ugly number**.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: An integer representing the `n-th` ugly number.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 10
```

**Output:**
```text
12
```

**Explanation:**
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

### Example 2

**Input:**
```text
n = 1
```

**Output:**
```text
1
```

**Explanation:**
1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

### Example 3

**Input:**
```text
n = 11
```

**Output:**
```text
15
```

**Explanation:**
11th ugly number is 15.

---

## Constraints

- `1 <= n <= 1690`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
