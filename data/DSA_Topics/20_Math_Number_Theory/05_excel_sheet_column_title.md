# 5. Excel Sheet Column Title

**Topic**: Math & Number Theory  
**Difficulty**: Easy  
**Tags**: Math, String

---

## Problem Statement

Given an integer `columnNumber`, return its corresponding column title as it appears in an Excel sheet.

For example:
`1 -> "A"`, `2 -> "B"`, `26 -> "Z"`, `27 -> "AA"`, `28 -> "AB"`, `701 -> "ZY"`.

---

## Input & Output Format

- **Input**: An integer `columnNumber`.
- **Output**: A string representing the column title.

---

## Sample Test Cases

### Example 1

**Input:**
```text
columnNumber = 1
```

**Output:**
```text
"A"
```

**Explanation:**
1 corresponds to 'A'.

### Example 2

**Input:**
```text
columnNumber = 28
```

**Output:**
```text
"AB"
```

**Explanation:**
28 = 26 * 1 + 2 -> "AB".

### Example 3

**Input:**
```text
columnNumber = 701
```

**Output:**
```text
"ZY"
```

**Explanation:**
701 = 26 * 26 + 25 -> "ZY".

---

## Constraints

- `1 <= columnNumber <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(log26(N))`
- **Space Complexity**: `O(1)`
