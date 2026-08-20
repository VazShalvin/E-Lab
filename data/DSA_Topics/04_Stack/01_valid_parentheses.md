# 1. Valid Parentheses

**Topic**: Stack  
**Difficulty**: Easy  
**Tags**: String, Stack

---

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

---

## Input & Output Format

- **Input**: A string `s`.
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
Simple matched parentheses.

### Example 2

**Input:**
```text
s = "()[]{}"
```

**Output:**
```text
true
```

**Explanation:**
All bracket types properly matched in order.

### Example 3

**Input:**
```text
s = "(]"
```

**Output:**
```text
false
```

**Explanation:**
Mismatched bracket types '(' and ']'.

---

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
