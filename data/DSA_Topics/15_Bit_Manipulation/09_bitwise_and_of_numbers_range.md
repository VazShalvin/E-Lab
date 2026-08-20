# 9. Bitwise AND of Numbers Range

**Topic**: Bit Manipulation  
**Difficulty**: Medium  
**Tags**: Bit Manipulation

---

## Problem Statement

Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

---

## Input & Output Format

- **Input**: Two integers `left` and `right`.
- **Output**: An integer representing the bitwise AND over the range.

---

## Sample Test Cases

### Example 1

**Input:**
```text
left = 5, right = 7
```

**Output:**
```text
4
```

**Explanation:**
5 & 6 & 7 = 101 & 110 & 111 = 100 (decimal 4).

### Example 2

**Input:**
```text
left = 0, right = 0
```

**Output:**
```text
0
```

**Explanation:**
0 & 0 = 0.

### Example 3

**Input:**
```text
left = 1, right = 2147483647
```

**Output:**
```text
0
```

**Explanation:**
All bits are cleared over large ranges except common prefix.

---

## Constraints

- `0 <= left <= right <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(1) (<= 32 shifts)`
- **Space Complexity**: `O(1)`
