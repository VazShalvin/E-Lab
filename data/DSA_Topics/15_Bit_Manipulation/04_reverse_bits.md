# 4. Reverse Bits

**Topic**: Bit Manipulation  
**Difficulty**: Easy  
**Tags**: Divide and Conquer, Bit Manipulation

---

## Problem Statement

Reverse bits of a given 32 bits unsigned integer.

---

## Input & Output Format

- **Input**: An unsigned 32-bit integer `n`.
- **Output**: The decimal value of the reversed 32-bit binary integer.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 00000010100101000001111010011100 (decimal: 43261596)
```

**Output:**
```text
964176192 (binary: 00111001011110000010100101000000)
```

**Explanation:**
Reversing all 32 bits.

### Example 2

**Input:**
```text
n = 11111111111111111111111111111101 (decimal: 4294967293)
```

**Output:**
```text
3221225471
```

**Explanation:**
Reversed bits evaluate to 3221225471.

### Example 3

**Input:**
```text
n = 0
```

**Output:**
```text
0
```

**Explanation:**
Reversed 32 zeros is 0.

---

## Constraints

- The input must be a binary string of length `32` or a 32-bit integer.

---

## Complexity Analysis

- **Time Complexity**: `O(1) (32 operations)`
- **Space Complexity**: `O(1)`
