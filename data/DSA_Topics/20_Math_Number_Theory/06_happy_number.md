# 6. Happy Number (Floyd's Cycle Detection)

**Topic**: Math & Number Theory  
**Difficulty**: Easy  
**Tags**: Hash Table, Math, Two Pointers

---

## Problem Statement

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1** are happy.

Return `true` if `n` is a happy number, and `false` if not.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 19
```

**Output:**
```text
true
```

**Explanation:**
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1 (Happy number!).

### Example 2

**Input:**
```text
n = 2
```

**Output:**
```text
false
```

**Explanation:**
Cycles endlessly: 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4.

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
1 is happy.

---

## Constraints

- `1 <= n <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
