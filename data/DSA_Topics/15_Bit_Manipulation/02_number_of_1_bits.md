# 2. Number of 1 Bits (Hamming Weight)

**Topic**: Bit Manipulation  
**Difficulty**: Easy  
**Tags**: Divide and Conquer, Bit Manipulation

---

## Problem Statement

Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the **Hamming weight**).

---

## Input & Output Format

- **Input**: A positive integer `n`.
- **Output**: An integer representing the count of set bits.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 11 (binary: 00000000000000000000000000001011)
```

**Output:**
```text
3
```

**Explanation:**
The input binary string has a total of three '1' bits.

### Example 2

**Input:**
```text
n = 128 (binary: 00000000000000000000000010000000)
```

**Output:**
```text
1
```

**Explanation:**
The input binary string has a total of one '1' bit.

### Example 3

**Input:**
```text
n = 2147483645
```

**Output:**
```text
30
```

**Explanation:**
Contains 30 set bits.

---

## Constraints

- The input must be a binary string of length `32` or a 32-bit unsigned integer.

---

## Complexity Analysis

- **Time Complexity**: `O(k) where k is number of set bits (using n & (n - 1))`
- **Space Complexity**: `O(1)`
