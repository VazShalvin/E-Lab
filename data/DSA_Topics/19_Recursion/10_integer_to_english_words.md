# 10. Integer to English Words

**Topic**: Recursion  
**Difficulty**: Hard  
**Tags**: Math, String, Recursion

---

## Problem Statement

Convert a non-negative integer `num` to its English words representation.

---

## Input & Output Format

- **Input**: An integer `num`.
- **Output**: A string representing the number in words.

---

## Sample Test Cases

### Example 1

**Input:**
```text
num = 123
```

**Output:**
```text
"One Hundred Twenty Three"
```

**Explanation:**
Converted to words.

### Example 2

**Input:**
```text
num = 12345
```

**Output:**
```text
"Twelve Thousand Three Hundred Forty Five"
```

**Explanation:**
Grouped by thousands recursively.

### Example 3

**Input:**
```text
num = 1234567
```

**Output:**
```text
"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

**Explanation:**
Grouped into Millions and Thousands.

---

## Constraints

- `0 <= num <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(1) (<= 10 digits)`
- **Space Complexity**: `O(1)`
