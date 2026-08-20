# 11. Expression Add Operators

**Topic**: Recursion  
**Difficulty**: Hard  
**Tags**: Math, String, Backtracking

---

## Problem Statement

Given a string `num` that contains only digits and an integer `target`, return **all possibilities** to insert the binary operators `'+'`, `'-'`, and/or `'*'` between the digits of `num` so that the resultant expression evaluates to the `target` value.

Note that operands in the returned expressions should not contain leading zeros.

---

## Input & Output Format

- **Input**: A string `num` and an integer `target`.
- **Output**: An array of valid expression strings.

---

## Sample Test Cases

### Example 1

**Input:**
```text
num = "123", target = 6
```

**Output:**
```text
["1*2*3", "1+2+3"]
```

**Explanation:**
Both 1*2*3 and 1+2+3 evaluate to 6.

### Example 2

**Input:**
```text
num = "232", target = 8
```

**Output:**
```text
["2*3+2", "2+3*2"]
```

**Explanation:**
Multiplication precedence handled with multed parameter.

### Example 3

**Input:**
```text
num = "3456237490", target = 9191
```

**Output:**
```text
[]
```

**Explanation:**
No valid expression.

---

## Constraints

- `1 <= num.length <= 10`
- `num` consists of only digits.
- `-2^31 <= target <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(4^N)`
- **Space Complexity**: `O(N)`
