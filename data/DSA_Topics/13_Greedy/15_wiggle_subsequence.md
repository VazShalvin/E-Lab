# 15. Wiggle Subsequence

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Greedy

---

## Problem Statement

A **wiggle sequence** is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

Given an integer array `nums`, return the length of the longest **wiggle subsequence** of `nums`.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing max wiggle subsequence length.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 7, 4, 9, 2, 5]
```

**Output:**
```text
6
```

**Explanation:**
The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

### Example 2

**Input:**
```text
nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
```

**Output:**
```text
7
```

**Explanation:**
Subsequence [1, 17, 10, 13, 10, 16, 8] has length 7.

### Example 3

**Input:**
```text
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Output:**
```text
2
```

**Explanation:**
Any 2 non-equal elements form a wiggle sequence of length 2.

---

## Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
