# 12. Parse Lisp Expression

**Topic**: Recursion  
**Difficulty**: Hard  
**Tags**: Hash Table, String, Stack, Recursion

---

## Problem Statement

You are given a string expression representing a Lisp-like expression to return the integer value of it.

The syntax of the expression is either an integer, `(let v1 e1 v2 e2 ... vn en expr)`, `(add e1 e2)`, or `(mult e1 e2)`.

Scoped variable environments must be maintained recursively.

---

## Input & Output Format

- **Input**: A string `expression`.
- **Output**: An integer representing the evaluated expression.

---

## Sample Test Cases

### Example 1

**Input:**
```text
expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
```

**Output:**
```text
14
```

**Explanation:**
In the inner let x = 3, y = 4, (add x y) = 7. In the outer let x = 2, (mult 2 7) = 14.

### Example 2

**Input:**
```text
expression = "(let x 3 x 2 x)"
```

**Output:**
```text
2
```

**Explanation:**
x reassigned to 2.

### Example 3

**Input:**
```text
expression = "(let x 1 y 2 x (add x y) (add x y))"
```

**Output:**
```text
5
```

**Explanation:**
x = 1, y = 2, x reassigned to (add 1 2) = 3, (add 3 2) = 5.

---

## Constraints

- `1 <= expression.length <= 2000`
- There are no spaces between parenthesis and commands, all tokens separated by single space.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
