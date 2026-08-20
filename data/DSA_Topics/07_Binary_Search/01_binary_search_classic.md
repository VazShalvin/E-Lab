# 1. Binary Search (Classic)

**Topic**: Binary Search  
**Difficulty**: Easy  
**Tags**: Array, Binary Search

---

## Problem Statement

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

---

## Input & Output Format

- **Input**: Sorted integer array `nums` and integer `target`.
- **Output**: An integer index, or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [-1, 0, 3, 5, 9, 12], target = 9
```

**Output:**
```text
4
```

**Explanation:**
9 exists in nums and its index is 4.

### Example 2

**Input:**
```text
nums = [-1, 0, 3, 5, 9, 12], target = 2
```

**Output:**
```text
-1
```

**Explanation:**
2 does not exist in nums so return -1.

### Example 3

**Input:**
```text
nums = [5], target = 5
```

**Output:**
```text
0
```

**Explanation:**
5 exists at index 0.

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
