# 13. Minimum Flips to Make a OR b Equal to c

**Topic**: Bit Manipulation  
**Difficulty**: Medium  
**Tags**: Bit Manipulation

---

## Problem Statement

Given 3 positives numbers `a`, `b` and `c`. Return the minimum flips required in some bits of `a` and `b` to make `(a OR b == c)` (bitwise OR operation).

Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

---

## Input & Output Format

- **Input**: Three integers `a`, `b`, and `c`.
- **Output**: An integer representing the minimum number of bit flips.

---

## Sample Test Cases

### Example 1

**Input:**
```text
a = 2, b = 6, c = 5
```

**Output:**
```text
3
```

**Explanation:**
After flips a = 1, b = 4, c = 5 such that (a OR b == c). Total 3 flips.

### Example 2

**Input:**
```text
a = 4, b = 2, c = 7
```

**Output:**
```text
1
```

**Explanation:**
Flip bit 0 of either a or b to 1.

### Example 3

**Input:**
```text
a = 1, b = 2, c = 3
```

**Output:**
```text
0
```

**Explanation:**
1 OR 2 = 3 already, 0 flips needed.

---

## Constraints

- `1 <= a <= 10^9`
- `1 <= b <= 10^9`
- `1 <= c <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`
