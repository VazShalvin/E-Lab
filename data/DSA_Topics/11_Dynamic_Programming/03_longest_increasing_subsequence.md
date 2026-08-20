# 3. Longest Increasing Subsequence (LIS)

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: Array, Binary Search, Dynamic Programming

---

## Problem Statement

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A **subsequence** is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the length of the longest increasing subsequence.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [10, 9, 2, 5, 3, 7, 101, 18]
```

**Output:**
```text
4
```

**Explanation:**
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.

### Example 2

**Input:**
```text
nums = [0, 1, 0, 3, 2, 3]
```

**Output:**
```text
4
```

**Explanation:**
[0, 1, 2, 3] has length 4.

### Example 3

**Input:**
```text
nums = [7, 7, 7, 7, 7, 7, 7]
```

**Output:**
```text
1
```

**Explanation:**
Strictly increasing subsequence of equal elements has length 1.

---

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N) with Binary Search or O(N^2) DP`
- **Space Complexity**: `O(N)`
