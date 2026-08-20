# 14. Rotate Array

**Topic**: Array  
**Difficulty**: Medium  
**Tags**: Array, Math, Two Pointers

---

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

Try to do it in-place with `O(1)` extra space.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `k`.
- **Output**: Modified array `nums` rotated right by `k` positions.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 3, 4, 5, 6, 7], k = 3
```

**Output:**
```text
[5, 6, 7, 1, 2, 3, 4]
```

**Explanation:**
rotate 1 steps to the right: [7, 1, 2, 3, 4, 5, 6]
rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5]
rotate 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]

### Example 2

**Input:**
```text
nums = [-1, -100, 3, 99], k = 2
```

**Output:**
```text
[3, 99, -1, -100]
```

**Explanation:**
rotate 1 steps to the right: [99, -1, -100, 3]
rotate 2 steps to the right: [3, 99, -1, -100]

### Example 3

**Input:**
```text
nums = [1, 2], k = 3
```

**Output:**
```text
[2, 1]
```

**Explanation:**
k = 3 is equivalent to k = 3 % 2 = 1 rotation.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
