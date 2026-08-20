# 8. Search in Rotated Sorted Array

**Topic**: Array  
**Difficulty**: Medium  
**Tags**: Array, Binary Search

---

## Problem Statement

There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `target`.
- **Output**: An integer index, or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [4, 5, 6, 7, 0, 1, 2], target = 0
```

**Output:**
```text
4
```

**Explanation:**
0 exists at index 4.

### Example 2

**Input:**
```text
nums = [4, 5, 6, 7, 0, 1, 2], target = 3
```

**Output:**
```text
-1
```

**Explanation:**
3 does not exist in nums.

### Example 3

**Input:**
```text
nums = [1], target = 0
```

**Output:**
```text
-1
```

**Explanation:**
0 does not exist in [1].

---

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique.
- `nums` is an ascending array that is possibly rotated.

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
