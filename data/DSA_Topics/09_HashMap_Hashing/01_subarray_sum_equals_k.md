# 1. Subarray Sum Equals K

**Topic**: HashMap / Hashing  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Prefix Sum

---

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `k`.
- **Output**: An integer count of subarrays.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 1, 1], k = 2
```

**Output:**
```text
2
```

**Explanation:**
Subarrays [1, 1] at indices [0, 1] and [1, 2] both sum to 2.

### Example 2

**Input:**
```text
nums = [1, 2, 3], k = 3
```

**Output:**
```text
2
```

**Explanation:**
[1, 2] and [3] sum to 3.

### Example 3

**Input:**
```text
nums = [1, -1, 0], k = 0
```

**Output:**
```text
3
```

**Explanation:**
[1, -1], [0], and [1, -1, 0] all sum to 0.

---

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
