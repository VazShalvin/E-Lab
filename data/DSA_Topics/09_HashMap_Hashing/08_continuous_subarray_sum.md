# 8. Continuous Subarray Sum

**Topic**: HashMap / Hashing  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Math, Prefix Sum

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a **good subarray** or `false` otherwise.

A **good subarray** is a subarray where:
- its length is **at least two**, and
- the sum of the elements of the subarray is a multiple of `k`.

Note that a multiple of `k` is an integer `x` such that `x = n * k` where `n` is also an integer (0 is a multiple of any `k`).

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `k`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [23, 2, 4, 6, 7], k = 6
```

**Output:**
```text
true
```

**Explanation:**
[2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

### Example 2

**Input:**
```text
nums = [23, 2, 6, 4, 7], k = 6
```

**Output:**
```text
true
```

**Explanation:**
[23, 2, 6, 4, 7] is an array of sum 42 which is a multiple of 6.

### Example 3

**Input:**
```text
nums = [23, 2, 6, 4, 7], k = 13
```

**Output:**
```text
false
```

**Explanation:**
No good subarray sum is a multiple of 13.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= sum(nums[i]) <= 2^31 - 1`
- `1 <= k <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(min(N, k))`
