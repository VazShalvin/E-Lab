# 15. Multiply Strings

**Topic**: String  
**Difficulty**: Medium  
**Tags**: Math, String, Simulation

---

## Problem Statement

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

---

## Input & Output Format

- **Input**: Two strings `num1` and `num2`.
- **Output**: A string representing the product.

---

## Sample Test Cases

### Example 1

**Input:**
```text
num1 = "2", num2 = "3"
```

**Output:**
```text
"6"
```

**Explanation:**
2 * 3 = 6.

### Example 2

**Input:**
```text
num1 = "123", num2 = "456"
```

**Output:**
```text
"56088"
```

**Explanation:**
123 * 456 = 56088.

### Example 3

**Input:**
```text
num1 = "0", num2 = "52"
```

**Output:**
```text
"0"
```

**Explanation:**
0 * 52 = 0.

---

## Constraints

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zero, except the number 0 itself.

---

## Complexity Analysis

- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(N + M)`
