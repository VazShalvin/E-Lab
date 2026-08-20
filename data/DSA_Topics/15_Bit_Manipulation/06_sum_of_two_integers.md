# 6. Sum of Two Integers (Without + or -)

**Topic**: Bit Manipulation  
**Difficulty**: Medium  
**Tags**: Math, Bit Manipulation

---

## Problem Statement

Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

---

## Input & Output Format

- **Input**: Two integers `a` and `b`.
- **Output**: An integer representing the sum.

---

## Sample Test Cases

### Example 1

**Input:**
```text
a = 1, b = 2
```

**Output:**
```text
3
```

**Explanation:**
1 + 2 = 3 calculated via XOR (sum without carry) and AND<<1 (carry).

### Example 2

**Input:**
```text
a = 2, b = 3
```

**Output:**
```text
5
```

**Explanation:**
2 + 3 = 5.

### Example 3

**Input:**
```text
a = -1, b = 1
```

**Output:**
```text
0
```

**Explanation:**
-1 + 1 = 0.

---

## Constraints

- `-1000 <= a, b <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(1) (32 iterations max)`
- **Space Complexity**: `O(1)`
