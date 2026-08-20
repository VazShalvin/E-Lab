# 15. Squares of a Sorted Array

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Easy  
**Tags**: Array, Two Pointers, Sorting

---

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing** order, return an array of the squares of each number sorted in non-decreasing order.

Could you do this in `O(N)` time complexity using two pointers from the outer ends?

---

## Input & Output Format

- **Input**: A sorted array of integers `nums`.
- **Output**: An array of sorted squares.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [-4, -1, 0, 3, 10]
```

**Output:**
```text
[0, 1, 9, 16, 100]
```

**Explanation:**
After squaring: [16, 1, 0, 9, 100]. After sorting: [0, 1, 9, 16, 100].

### Example 2

**Input:**
```text
nums = [-7, -3, 2, 3, 11]
```

**Output:**
```text
[4, 9, 9, 49, 121]
```

**Explanation:**
Sorted squares.

### Example 3

**Input:**
```text
nums = [-1]
```

**Output:**
```text
[1]
```

**Explanation:**
(-1)^2 = 1.

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
