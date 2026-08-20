# 1. Merge Sort & Count Inversions

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, Divide and Conquer, Sorting

---

## Problem Statement

Given an integer array `nums`, implement Merge Sort to sort the array in ascending order and also count the number of **inversions** in the array.

An inversion is a pair of indices `(i, j)` such that `i < j` and `nums[i] > nums[j]`.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: Sorted array and an integer representing the inversion count.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [8, 4, 2, 1]
```

**Output:**
```text
sorted: [1, 2, 4, 8], inversions: 6
```

**Explanation:**
Inversions are (8,4), (8,2), (8,1), (4,2), (4,1), (2,1). Total = 6.

### Example 2

**Input:**
```text
nums = [1, 20, 6, 4, 5]
```

**Output:**
```text
sorted: [1, 4, 5, 6, 20], inversions: 5
```

**Explanation:**
(20,6), (20,4), (20,5), (6,4), (6,5). Total = 5.

### Example 3

**Input:**
```text
nums = [1, 2, 3]
```

**Output:**
```text
sorted: [1, 2, 3], inversions: 0
```

**Explanation:**
Already sorted, 0 inversions.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
