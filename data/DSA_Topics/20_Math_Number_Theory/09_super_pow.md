# 9. Super Pow (Euler's Totient & Modular Arithmetic)

**Topic**: Math & Number Theory  
**Difficulty**: Medium  
**Tags**: Math, Divide and Conquer

---

## Problem Statement

Your task is to calculate `a^b mod 1337` where `a` is a positive integer and `b` is an extremely large positive integer given in the form of an array.

---

## Input & Output Format

- **Input**: An integer `a` and an array of digits `b`.
- **Output**: An integer representing `(a^b) % 1337`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
a = 2, b = [3]
```

**Output:**
```text
8
```

**Explanation:**
2^3 % 1337 = 8.

### Example 2

**Input:**
```text
a = 2, b = [1, 0]
```

**Output:**
```text
1024
```

**Explanation:**
2^10 % 1337 = 1024.

### Example 3

**Input:**
```text
a = 1, b = [4, 3, 3, 8, 5, 2]
```

**Output:**
```text
1
```

**Explanation:**
1 raised to any power is 1.

---

## Constraints

- `1 <= a <= 2^31 - 1`
- `1 <= b.length <= 2000`
- `0 <= b[i] <= 9`
- `b` does not contain leading zeros.

---

## Complexity Analysis

- **Time Complexity**: `O(len(b))`
- **Space Complexity**: `O(len(b))`
