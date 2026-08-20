# 11. Partition Equal Subset Sum (0/1 Knapsack)

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming

---

## Problem Statement

Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `false` otherwise.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 5, 11, 5]
```

**Output:**
```text
true
```

**Explanation:**
The array can be partitioned as [1, 5, 5] and [11], each summing to 11.

### Example 2

**Input:**
```text
nums = [1, 2, 3, 5]
```

**Output:**
```text
false
```

**Explanation:**
Total sum is 11 (odd), which cannot be split equally.

### Example 3

**Input:**
```text
nums = [2, 2]
```

**Output:**
```text
true
```

**Explanation:**
Split into [2] and [2].

---

## Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

---

## Complexity Analysis

- **Time Complexity**: `O(N * TargetSum)`
- **Space Complexity**: `O(TargetSum)`
