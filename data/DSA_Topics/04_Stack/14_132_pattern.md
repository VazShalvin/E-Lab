# 14. 132 Pattern

**Topic**: Stack  
**Difficulty**: Medium  
**Tags**: Array, Binary Search, Stack, Monotonic Stack

---

## Problem Statement

Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers `nums[i]`, `nums[j]` and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.

Return `true` if there is a **132 pattern** in `nums`, otherwise, return `false`.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 3, 4]
```

**Output:**
```text
false
```

**Explanation:**
There is no 132 pattern; sequence is strictly increasing.

### Example 2

**Input:**
```text
nums = [3, 1, 4, 2]
```

**Output:**
```text
true
```

**Explanation:**
Subsequence [1, 4, 2] forms a 132 pattern (1 < 2 < 4).

### Example 3

**Input:**
```text
nums = [-1, 3, 2, 0]
```

**Output:**
```text
true
```

**Explanation:**
Subsequences [-1, 3, 2], [-1, 3, 0] both satisfy the pattern.

---

## Constraints

- `n == nums.length`
- `1 <= n <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
