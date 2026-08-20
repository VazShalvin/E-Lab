# 14. Basic Calculator II

**Topic**: String  
**Difficulty**: Medium  
**Tags**: Math, String, Stack

---

## Problem Statement

Given a string `s` which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero. You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions.

---

## Input & Output Format

- **Input**: A string `s` containing non-negative integers and operators `+`, `-`, `*`, `/`.
- **Output**: An integer representing the evaluated expression.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "3+2*2"
```

**Output:**
```text
7
```

**Explanation:**
Multiplication has higher precedence: 3 + (2*2) = 7.

### Example 2

**Input:**
```text
s = " 3/2 "
```

**Output:**
```text
1
```

**Explanation:**
Integer division truncates: 3 / 2 = 1.

### Example 3

**Input:**
```text
s = " 3+5 / 2 "
```

**Output:**
```text
5
```

**Explanation:**
3 + (5/2) = 3 + 2 = 5.

---

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of integers and operators (`'+'`, `'-'`, `'*'`, `'/'`) separated by some number of spaces.
- `s` represents a valid expression.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
