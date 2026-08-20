# 13. Basic Calculator (Parentheses & Signs)

**Topic**: Stack  
**Difficulty**: Hard  
**Tags**: Math, String, Stack, Recursion

---

## Problem Statement

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions. Support `+`, `-`, `(`, `)`, digits and spaces.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: An integer representing the evaluated expression.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "1 + 1"
```

**Output:**
```text
2
```

**Explanation:**
1 + 1 = 2.

### Example 2

**Input:**
```text
s = " 2-1 + 2 "
```

**Output:**
```text
3
```

**Explanation:**
2 - 1 + 2 = 3.

### Example 3

**Input:**
```text
s = "(1+(4+5+2)-3)+(6+8)"
```

**Output:**
```text
23
```

**Explanation:**
(1 + 11 - 3) + 14 = 9 + 14 = 23.

---

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
- `s` represents a valid expression.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
