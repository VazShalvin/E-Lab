# 7. Maximum Gap (Bucket / Radix Sort)

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, Sorting, Bucket Sort, Radix Sort

---

## Problem Statement

Given an integer array `nums`, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return `0`.

You must write an algorithm that runs in `O(n)` time and uses `O(n)` extra space using Bucket Sort / Pigeonhole principle.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the maximum gap.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [3, 6, 9, 1]
```

**Output:**
```text
3
```

**Explanation:**
The sorted form of the array is [1, 3, 6, 9], either (3, 6) or (6, 9) has the maximum difference 3.

### Example 2

**Input:**
```text
nums = [10]
```

**Output:**
```text
0
```

**Explanation:**
Array contains less than 2 elements, return 0.

### Example 3

**Input:**
```text
nums = [1, 10000000]
```

**Output:**
```text
9999999
```

**Explanation:**
Gap is 10000000 - 1 = 9999999.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
