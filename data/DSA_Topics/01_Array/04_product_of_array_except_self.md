# 4. Product of Array Except Self

**Topic**: Array  
**Difficulty**: Medium  
**Tags**: Array, Prefix Sum

---

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An array of integers `answer` where `answer[i]` is the product of all elements except `nums[i]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 3, 4]
```

**Output:**
```text
[24, 12, 8, 6]
```

**Explanation:**
answer[0] = 2*3*4 = 24
answer[1] = 1*3*4 = 12
answer[2] = 1*2*4 = 8
answer[3] = 1*2*3 = 6

### Example 2

**Input:**
```text
nums = [-1, 1, 0, -3, 3]
```

**Output:**
```text
[0, 0, 9, 0, 0]
```

**Explanation:**
For index 2 (value 0), product of rest is (-1)*1*(-3)*3 = 9. For all other indices, the product contains 0.

### Example 3

**Input:**
```text
nums = [2, 3, 5]
```

**Output:**
```text
[15, 10, 6]
```

**Explanation:**
answer = [3*5, 2*5, 2*3] = [15, 10, 6].

---

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) extra space`
