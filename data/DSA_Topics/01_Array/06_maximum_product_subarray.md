# 6. Maximum Product Subarray

**Topic**: Array  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming

---

## Problem Statement

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the largest contiguous product.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [2, 3, -2, 4]
```

**Output:**
```text
6
```

**Explanation:**
[2, 3] has the largest product 6.

### Example 2

**Input:**
```text
nums = [-2, 0, -1]
```

**Output:**
```text
0
```

**Explanation:**
The result cannot be 2, because [-2, -1] is not a contiguous subarray.

### Example 3

**Input:**
```text
nums = [-2, 3, -4]
```

**Output:**
```text
24
```

**Explanation:**
The entire array [-2, 3, -4] has product (-2) * 3 * (-4) = 24.

---

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
