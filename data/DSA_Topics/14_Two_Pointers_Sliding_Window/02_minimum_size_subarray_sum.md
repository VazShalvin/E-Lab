# 2. Minimum Size Subarray Sum

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Array, Binary Search, Sliding Window, Prefix Sum

---

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

---

## Input & Output Format

- **Input**: An integer `target` and an array of integers `nums`.
- **Output**: An integer representing minimum subarray length.

---

## Sample Test Cases

### Example 1

**Input:**
```text
target = 7, nums = [2, 3, 1, 2, 4, 3]
```

**Output:**
```text
2
```

**Explanation:**
The subarray [4, 3] has the minimal length under the problem constraint.

### Example 2

**Input:**
```text
target = 4, nums = [1, 4, 4]
```

**Output:**
```text
1
```

**Explanation:**
[4] has length 1.

### Example 3

**Input:**
```text
target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
```

**Output:**
```text
0
```

**Explanation:**
Total sum is 8 < 11.

---

## Constraints

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
