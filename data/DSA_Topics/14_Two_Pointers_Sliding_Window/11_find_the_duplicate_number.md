# 11. Find the Duplicate Number (Floyd's Tortoise and Hare)

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Array, Two Pointers, Binary Search, Bit Manipulation

---

## Problem Statement

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return this repeated number.

You must solve the problem **without** modifying the array `nums` and uses only constant `O(1)` extra space.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the duplicate number.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 3, 4, 2, 2]
```

**Output:**
```text
2
```

**Explanation:**
2 is the duplicate number.

### Example 2

**Input:**
```text
nums = [3, 1, 3, 4, 2]
```

**Output:**
```text
3
```

**Explanation:**
3 is the duplicate number.

### Example 3

**Input:**
```text
nums = [3, 3, 3, 3, 3]
```

**Output:**
```text
3
```

**Explanation:**
3 is repeated.

---

## Constraints

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
