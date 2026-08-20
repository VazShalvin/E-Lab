# 8. Find First and Last Position of Element in Sorted Array

**Topic**: Binary Search  
**Difficulty**: Medium  
**Tags**: Array, Binary Search

---

## Problem Statement

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `target`.
- **Output**: An array of two integers `[firstIndex, lastIndex]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [5, 7, 7, 8, 8, 10], target = 8
```

**Output:**
```text
[3, 4]
```

**Explanation:**
8 appears starting at index 3 and ending at index 4.

### Example 2

**Input:**
```text
nums = [5, 7, 7, 8, 8, 10], target = 6
```

**Output:**
```text
[-1, -1]
```

**Explanation:**
6 does not exist in nums.

### Example 3

**Input:**
```text
nums = [], target = 0
```

**Output:**
```text
[-1, -1]
```

**Explanation:**
Empty array returns [-1, -1].

---

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
