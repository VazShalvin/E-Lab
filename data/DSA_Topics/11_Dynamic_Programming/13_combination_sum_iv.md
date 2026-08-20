# 13. Combination Sum IV

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Memoization

---

## Problem Statement

Given an array of **distinct** integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`.

Note that different sequences are counted as different combinations.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `target`.
- **Output**: An integer representing total combinations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 3], target = 4
```

**Output:**
```text
7
```

**Explanation:**
The possible combinations are:
(1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 3), (2, 1, 1), (2, 2), (3, 1). Total 7.

### Example 2

**Input:**
```text
nums = [9], target = 3
```

**Output:**
```text
0
```

**Explanation:**
Cannot form 3 using 9.

### Example 3

**Input:**
```text
nums = [1, 2], target = 3
```

**Output:**
```text
3
```

**Explanation:**
(1,1,1), (1,2), (2,1).

---

## Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 1000`
- All elements of `nums` are **unique**.
- `1 <= target <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(target * len(nums))`
- **Space Complexity**: `O(target)`
