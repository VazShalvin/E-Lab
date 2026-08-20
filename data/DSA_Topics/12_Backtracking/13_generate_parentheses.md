# 13. Generate Parentheses

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: String, Dynamic Programming, Backtracking

---

## Problem Statement

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: An array of well-formed parentheses strings.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 3
```

**Output:**
```text
["((()))", "(()())", "(())()", "()(())", "()()()"]
```

**Explanation:**
All 5 well-formed parentheses strings for n = 3.

### Example 2

**Input:**
```text
n = 1
```

**Output:**
```text
["()"]
```

**Explanation:**
Single valid combination.

### Example 3

**Input:**
```text
n = 2
```

**Output:**
```text
["(())", "()()"]
```

**Explanation:**
Two valid combinations for n = 2.

---

## Constraints

- `1 <= n <= 8`

---

## Complexity Analysis

- **Time Complexity**: `O(4^N / sqrt(N)) (Catalan number)`
- **Space Complexity**: `O(N)`
