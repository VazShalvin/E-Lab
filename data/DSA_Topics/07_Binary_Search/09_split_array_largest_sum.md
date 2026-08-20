# 9. Split Array Largest Sum

**Topic**: Binary Search  
**Difficulty**: Hard  
**Tags**: Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum

---

## Problem Statement

Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is **minimized**.

Return the minimized largest sum of the split.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `k`.
- **Output**: An integer representing the minimized largest sum.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [7, 2, 5, 10, 8], k = 2
```

**Output:**
```text
18
```

**Explanation:**
There are four ways to split nums into two subarrays. The best way is to split it into [7, 2, 5] and [10, 8], where the largest sum among the two subarrays is only 18.

### Example 2

**Input:**
```text
nums = [1, 2, 3, 4, 5], k = 2
```

**Output:**
```text
9
```

**Explanation:**
Split into [1, 2, 3] and [4, 5], max sum = 9.

### Example 3

**Input:**
```text
nums = [1, 4, 4], k = 3
```

**Output:**
```text
4
```

**Explanation:**
Split into [1], [4], [4], max sum = 4.

---

## Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 10^6`
- `1 <= k <= min(50, nums.length)`

---

## Complexity Analysis

- **Time Complexity**: `O(N log(sum(nums)))`
- **Space Complexity**: `O(1)`
