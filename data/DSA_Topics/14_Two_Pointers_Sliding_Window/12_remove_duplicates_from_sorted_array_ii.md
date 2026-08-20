# 12. Remove Duplicates from Sorted Array II (At Most Twice)

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Array, Two Pointers

---

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears **at most twice**. The relative order of the elements should be kept the same.

Return `k` after placing the final result in the first `k` slots of `nums`.

---

## Input & Output Format

- **Input**: A sorted array of integers `nums`.
- **Output**: An integer `k` representing the length of the valid prefix.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 1, 1, 2, 2, 3]
```

**Output:**
```text
5, nums = [1, 1, 2, 2, 3, _]
```

**Explanation:**
Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

### Example 2

**Input:**
```text
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
```

**Output:**
```text
7, nums = [0, 0, 1, 1, 2, 3, 3, _, _]
```

**Explanation:**
Your function returns k = 7.

### Example 3

**Input:**
```text
nums = [1, 1]
```

**Output:**
```text
2, nums = [1, 1]
```

**Explanation:**
No modification needed.

---

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
