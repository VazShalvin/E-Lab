# 4. Subarrays with K Different Integers

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Hard  
**Tags**: Array, Hash Table, Sliding Window, Counting

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of **good subarrays** of `nums`.

A **good array** is an array where the number of different integers in that array is exactly `k`.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `k`.
- **Output**: An integer count of valid subarrays.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 1, 2, 3], k = 2
```

**Output:**
```text
7
```

**Explanation:**
Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

### Example 2

**Input:**
```text
nums = [1, 2, 1, 3, 4], k = 3
```

**Output:**
```text
3
```

**Explanation:**
Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

### Example 3

**Input:**
```text
nums = [1], k = 1
```

**Output:**
```text
1
```

**Explanation:**
[1] is the only valid subarray.

---

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `1 <= nums[i], k <= nums.length`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
