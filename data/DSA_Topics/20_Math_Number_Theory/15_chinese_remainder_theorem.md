# 15. Chinese Remainder Theorem

**Topic**: Math & Number Theory  
**Difficulty**: Hard  
**Tags**: Math, Number Theory

---

## Problem Statement

Given two arrays of integers `num[0..k-1]` and `rem[0..k-1]`, find the smallest positive integer `x` such that `x % num[i] = rem[i]` for all `0 <= i < k`.

All elements of `num` are **pairwise coprime**.

---

## Input & Output Format

- **Input**: Two arrays `num` and `rem`.
- **Output**: An integer representing the smallest positive `x`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
num = [3, 4, 5], rem = [2, 3, 1]
```

**Output:**
```text
11
```

**Explanation:**
11 is the smallest number that:
- leaves remainder 2 when divided by 3
- leaves remainder 3 when divided by 4
- leaves remainder 1 when divided by 5

### Example 2

**Input:**
```text
num = [5, 7], rem = [1, 3]
```

**Output:**
```text
31
```

**Explanation:**
31 % 5 = 1, 31 % 7 = 3.

### Example 3

**Input:**
```text
num = [2, 3], rem = [1, 2]
```

**Output:**
```text
5
```

**Explanation:**
5 % 2 = 1, 5 % 3 = 2.

---

## Constraints

- `1 <= k <= 10`
- `1 <= num[i] <= 100`
- `0 <= rem[i] < num[i]`
- All `num[i]` are pairwise coprime.

---

## Complexity Analysis

- **Time Complexity**: `O(k * log(prod(num)))`
- **Space Complexity**: `O(k)`
