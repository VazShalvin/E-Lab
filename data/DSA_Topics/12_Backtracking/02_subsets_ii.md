# 2. Subsets II (With Duplicates)

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: Array, Backtracking, Bit Manipulation

---

## Problem Statement

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: A 2D array of unique subsets.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 2]
```

**Output:**
```text
[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
```

**Explanation:**
Duplicate subsets like second [2] are skipped.

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
Unique subsets.

### Example 3

**Input:**
```text
nums = [4, 4, 4, 1, 4]
```

**Output:**
```text
[[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]
```

**Explanation:**
Generates all distinct subsets.

---

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

---

## Complexity Analysis

- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(N)`
