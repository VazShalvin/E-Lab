# 1. Subsets (Power Set)

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: Array, Backtracking, Bit Manipulation

---

## Problem Statement

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: A 2D array of all possible subsets.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 3]
```

**Output:**
```text
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

**Explanation:**
All 2^3 = 8 subsets.

### Example 2

**Input:**
```text
nums = [0]
```

**Output:**
```text
[[], [0]]
```

**Explanation:**
2^1 = 2 subsets.

### Example 3

**Input:**
```text
nums = [1, 2]
```

**Output:**
```text
[[], [1], [2], [1, 2]]
```

**Explanation:**
All 4 subsets generated.

---

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

---

## Complexity Analysis

- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(N)`
