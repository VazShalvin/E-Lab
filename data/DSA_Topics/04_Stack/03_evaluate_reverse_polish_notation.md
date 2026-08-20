# 3. Evaluate Reverse Polish Notation

**Topic**: Stack  
**Difficulty**: Medium  
**Tags**: Array, Math, Stack

---

## Problem Statement

You are given an array of strings `tokens` that represents an arithmetic expression in a **Reverse Polish Notation**.

Evaluate the expression. Return an integer that represents the value of the expression.

Valid operators are `'+'`, `'-'`, `'*'`, and `'/'`. Division truncates toward zero.

---

## Input & Output Format

- **Input**: An array of strings `tokens`.
- **Output**: An integer representing evaluated expression result.

---

## Sample Test Cases

### Example 1

**Input:**
```text
tokens = ["2", "1", "+", "3", "*"]
```

**Output:**
```text
9
```

**Explanation:**
((2 + 1) * 3) = 9

### Example 2

**Input:**
```text
tokens = ["4", "13", "5", "/", "+"]
```

**Output:**
```text
6
```

**Explanation:**
(4 + (13 / 5)) = 4 + 2 = 6

### Example 3

**Input:**
```text
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
```

**Output:**
```text
22
```

**Explanation:**
Evaluates to 22.

---

## Constraints

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
