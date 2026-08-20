# 6. Different Ways to Add Parentheses

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: Math, String, Dynamic Programming, Recursion, Memoization

---

## Problem Statement

Given a string `expression` of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in **any order**.

---

## Input & Output Format

- **Input**: A string `expression` containing digits and operators `+`, `-`, `*`.
- **Output**: An array of integers representing all evaluated results.

---

## Sample Test Cases

### Example 1

**Input:**
```text
expression = "2-1-1"
```

**Output:**
```text
[0, 2]
```

**Explanation:**
((2-1)-1) = 0
(2-(1-1)) = 2

### Example 2

**Input:**
```text
expression = "2*3-4*5"
```

**Output:**
```text
[-34, -14, -10, -10, 10]
```

**Explanation:**
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

### Example 3

**Input:**
```text
expression = "5"
```

**Output:**
```text
[5]
```

**Explanation:**
Single number evaluation.

---

## Constraints

- `1 <= expression.length <= 20`
- `expression` consists of digits and the operator `'+'`, `'-'`, and `'*'`. 
- All integer values in the input expression are in the range `[0, 99]`.

---

## Complexity Analysis

- **Time Complexity**: `O(4^N / sqrt(N)) (Catalan number)`
- **Space Complexity**: `O(4^N / sqrt(N))`
