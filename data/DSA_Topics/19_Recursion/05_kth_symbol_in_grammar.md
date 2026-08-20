# 5. K-th Symbol in Grammar

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: Math, Bit Manipulation, Recursion

---

## Problem Statement

We build a table of `n` rows (**1-indexed**). We start by writing `0` in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `01`, and each occurrence of `1` with `10`.

Given two integers `n` and `k`, return the `k-th` (**1-indexed**) symbol in the `n-th` row of the table of `n` rows.

---

## Input & Output Format

- **Input**: Two integers `n` and `k`.
- **Output**: An integer (`0` or `1`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 1, k = 1
```

**Output:**
```text
0
```

**Explanation:**
Row 1: 0.

### Example 2

**Input:**
```text
n = 2, k = 1
```

**Output:**
```text
0
```

**Explanation:**
Row 1: 0
Row 2: 01
1st symbol is 0.

### Example 3

**Input:**
```text
n = 2, k = 2
```

**Output:**
```text
1
```

**Explanation:**
Row 2: 01, 2nd symbol is 1.

---

## Constraints

- `1 <= n <= 30`
- `1 <= k <= 2^(n - 1)`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N) recursion stack`
