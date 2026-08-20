# 4. Permutations II (With Duplicates)

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: Array, Backtracking

---

## Problem Statement

Given a collection of numbers, `nums`, that might contain duplicates, return all possible **unique** permutations in any order.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: A 2D array of unique permutations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 1, 2]
```

**Output:**
```text
[[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

**Explanation:**
3 unique permutations.

### Example 2

**Input:**
```text
nums = [1, 2, 3]
```

**Output:**
```text
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

**Explanation:**
All distinct elements.

### Example 3

**Input:**
```text
nums = [2, 2]
```

**Output:**
```text
[[2, 2]]
```

**Explanation:**
Single unique permutation.

---

## Constraints

- `1 <= nums.length <= 8`
- `-10 <= nums[i] <= 10`

---

## Complexity Analysis

- **Time Complexity**: `O(N * N!)`
- **Space Complexity**: `O(N)`
