# 11. String to Integer (atoi)

**Topic**: String  
**Difficulty**: Medium  
**Tags**: String

---

## Problem Statement

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:
1. Whitespace: Ignore any leading whitespace (`" "`).
2. Signedness: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, clamp it to the bounds.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: A 32-bit signed integer.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "42"
```

**Output:**
```text
42
```

**Explanation:**
The underlined characters are what is read in: "42".

### Example 2

**Input:**
```text
s = "   -42"
```

**Output:**
```text
-42
```

**Explanation:**
Leading whitespace ignored, '-' read, digits '42' parsed.

### Example 3

**Input:**
```text
s = "4193 with words"
```

**Output:**
```text
4193
```

**Explanation:**
Parsing stops at the space character as it is non-digit.

---

## Constraints

- `0 <= s.length <= 200`
- `s` consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
