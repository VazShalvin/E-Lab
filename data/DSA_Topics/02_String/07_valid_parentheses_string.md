# 7. Valid Parentheses String

**Topic**: String  
**Difficulty**: Medium  
**Tags**: String, Dynamic Programming, Stack, Greedy

---

## Problem Statement

Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` if `s` is **valid**.

The following rules define a valid string:
- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

---

## Input & Output Format

- **Input**: A string `s` containing `(`, `)`, and `*`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "()"
```

**Output:**
```text
true
```

**Explanation:**
Valid balanced parentheses.

### Example 2

**Input:**
```text
s = "(*)"
```

**Output:**
```text
true
```

**Explanation:**
The '*' acts as an empty string.

### Example 3

**Input:**
```text
s = "(*))"
```

**Output:**
```text
true
```

**Explanation:**
The '*' acts as '(' to match the extra ')'.

---

## Constraints

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`. 

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
