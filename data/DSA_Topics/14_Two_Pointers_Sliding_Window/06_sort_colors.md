# 6. Sort Colors (Dutch National Flag Algorithm)

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Array, Two Pointers, Sorting

---

## Problem Statement

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function and in one pass with `O(1)` space.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: Modified array sorted in-place `[0, ..., 1, ..., 2, ...]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [2, 0, 2, 1, 1, 0]
```

**Output:**
```text
[0, 0, 1, 1, 2, 2]
```

**Explanation:**
All 0s first, then 1s, then 2s.

### Example 2

**Input:**
```text
nums = [2, 0, 1]
```

**Output:**
```text
[0, 1, 2]
```

**Explanation:**
Sorted in non-decreasing order.

### Example 3

**Input:**
```text
nums = [0]
```

**Output:**
```text
[0]
```

**Explanation:**
Single element remains [0].

---

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

---

## Complexity Analysis

- **Time Complexity**: `O(N) single pass`
- **Space Complexity**: `O(1)`
