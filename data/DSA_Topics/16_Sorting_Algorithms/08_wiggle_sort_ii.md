# 8. Wiggle Sort II

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, Divide and Conquer, Sorting, Quickselect

---

## Problem Statement

Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`.

You may assume the input array always has a valid answer.

Can you do it in `O(n)` time and/or `O(1)` extra space?

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: Modified array reordered in wiggle pattern in-place.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 5, 1, 1, 6, 4]
```

**Output:**
```text
[1, 6, 1, 5, 1, 4]
```

**Explanation:**
[1, 4, 1, 5, 1, 6] is also accepted.

### Example 2

**Input:**
```text
nums = [1, 3, 2, 2, 3, 1]
```

**Output:**
```text
[2, 3, 1, 3, 1, 2]
```

**Explanation:**
Valid wiggle arrangement.

### Example 3

**Input:**
```text
nums = [1, 1, 2, 2, 3, 3]
```

**Output:**
```text
[2, 3, 1, 3, 1, 2]
```

**Explanation:**
Separates duplicate median elements.

---

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5000`

---

## Complexity Analysis

- **Time Complexity**: `O(N) with QuickSelect median finding`
- **Space Complexity**: `O(N) or O(1) with virtual indexing`
