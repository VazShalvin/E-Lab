# 3. Permutations

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: Array, Backtracking

---

## Problem Statement

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: A 2D array of all permutations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 3]
```

**Output:**
```text
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

**Explanation:**
All 3! = 6 permutations generated.

### Example 2

**Input:**
```text
nums = [0, 1]
```

**Output:**
```text
[[0, 1], [1, 0]]
```

**Explanation:**
2 permutations.

### Example 3

**Input:**
```text
nums = [1]
```

**Output:**
```text
[[1]]
```

**Explanation:**
Single permutation.

---

## Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All integers in `nums` are **unique**.

---

## Complexity Analysis

- **Time Complexity**: `O(N * N!)`
- **Space Complexity**: `O(N)`
