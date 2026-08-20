# 15. Target Sum (+/- Assignment DP)

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Backtracking

---

## Problem Statement

You are given an integer array `nums` and an integer `target`.

You want to build an expression out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

Return the number of different expressions that you can build, which evaluates to `target`.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `target`.
- **Output**: An integer count of valid expressions.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 1, 1, 1, 1], target = 3
```

**Output:**
```text
5
```

**Explanation:**
5 ways:
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

### Example 2

**Input:**
```text
nums = [1], target = 1
```

**Output:**
```text
1
```

**Explanation:**
+1 = 1.

### Example 3

**Input:**
```text
nums = [1, 0], target = 1
```

**Output:**
```text
2
```

**Explanation:**
+1+0 and +1-0 both evaluate to 1.

---

## Constraints

- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `0 <= sum(nums[i]) <= 1000`
- `-1000 <= target <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N * Sum)`
- **Space Complexity**: `O(Sum)`
