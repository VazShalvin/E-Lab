# 14. Matrix Chain Multiplication

**Topic**: Dynamic Programming  
**Difficulty**: Hard  
**Tags**: Array, Dynamic Programming

---

## Problem Statement

Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

Given an array `p` of numbers such that matrix `A_i` has dimension `p[i-1] x p[i]`, find the minimum number of scalar multiplications needed to multiply the chain.

---

## Input & Output Format

- **Input**: An integer array `p` representing matrix dimensions.
- **Output**: An integer representing the minimum multiplications.

---

## Sample Test Cases

### Example 1

**Input:**
```text
p = [40, 20, 30, 10, 30]
```

**Output:**
```text
26000
```

**Explanation:**
Multiplication order ((A(BC))D) gives 20*30*10 + 40*20*10 + 40*10*30 = 6000 + 8000 + 12000 = 26000 operations.

### Example 2

**Input:**
```text
p = [10, 20, 30, 40, 30]
```

**Output:**
```text
30000
```

**Explanation:**
Optimal parenthesization requires 30000 operations.

### Example 3

**Input:**
```text
p = [10, 30, 5]
```

**Output:**
```text
1500
```

**Explanation:**
Single multiplication of matrices 10x30 and 30x5 gives 10 * 30 * 5 = 1500.

---

## Constraints

- `2 <= p.length <= 100`
- `1 <= p[i] <= 500`

---

## Complexity Analysis

- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`
