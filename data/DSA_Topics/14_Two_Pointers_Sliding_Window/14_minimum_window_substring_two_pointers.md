# 14. Find All Subarrays with Bounded Maximum

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Array, Two Pointers

---

## Problem Statement

Given an integer array `nums` and two integers `left` and `right`, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range `[left, right]`.

---

## Input & Output Format

- **Input**: An array of integers `nums` and integers `left`, `right`.
- **Output**: An integer count of subarrays.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [2, 1, 4, 3], left = 2, right = 3
```

**Output:**
```text
3
```

**Explanation:**
There are three subarrays that meet the requirements: [2], [2, 1], [3].

### Example 2

**Input:**
```text
nums = [2, 9, 2, 5, 6], left = 2, right = 8
```

**Output:**
```text
7
```

**Explanation:**
7 valid subarrays bounded in [2, 8].

### Example 3

**Input:**
```text
nums = [7], left = 2, right = 8
```

**Output:**
```text
1
```

**Explanation:**
[7] is bounded.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= left <= right <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
