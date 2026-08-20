# 11. Shortest Subarray with Sum at Least K

**Topic**: Queue  
**Difficulty**: Hard  
**Tags**: Array, Binary Search, Queue, Sliding Window, Heap, Prefix Sum, Monotonic Queue

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return the length of the shortest non-empty subarray of `nums` with a sum of at least `k`. If there is no such subarray, return `-1`.

A **subarray** is a contiguous part of an array.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `k`.
- **Output**: An integer length or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1], k = 1
```

**Output:**
```text
1
```

**Explanation:**
The subarray [1] has sum 1 >= 1.

### Example 2

**Input:**
```text
nums = [1, 2], k = 4
```

**Output:**
```text
-1
```

**Explanation:**
Total sum is 3, which is less than 4.

### Example 3

**Input:**
```text
nums = [2, -1, 2], k = 3
```

**Output:**
```text
3
```

**Explanation:**
Subarray [2, -1, 2] has sum 3 >= 3, shortest length is 3.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
