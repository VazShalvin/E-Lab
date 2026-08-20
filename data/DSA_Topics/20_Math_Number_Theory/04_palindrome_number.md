# 4. Palindrome Number (Without String Conversion)

**Topic**: Math & Number Theory  
**Difficulty**: Easy  
**Tags**: Math

---

## Problem Statement

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

Could you solve it without converting the integer to a string by reversing only the second half of the digits?

---

## Input & Output Format

- **Input**: An integer `x`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
x = 121
```

**Output:**
```text
true
```

**Explanation:**
121 reads as 121 from left to right and from right to left.

### Example 2

**Input:**
```text
x = -121
```

**Output:**
```text
false
```

**Explanation:**
From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

### Example 3

**Input:**
```text
x = 10
```

**Output:**
```text
false
```

**Explanation:**
Reads 01 from right to left.

---

## Constraints

- `-2^31 <= x <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(log10(x))`
- **Space Complexity**: `O(1)`
