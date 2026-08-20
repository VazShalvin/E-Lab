# 1. Two Sum

**Topic**: Array  
**Difficulty**: Easy  
**Tags**: Array, Hash Table

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

---

## Input & Output Format

- **Input**: An integer array `nums` and an integer `target`.
- **Output**: An array of two integers representing indices `[index1, index2]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [2, 7, 11, 15], target = 9
```

**Output:**
```text
[0, 1]
```

**Explanation:**
Because nums[0] + nums[1] == 2 + 7 == 9, we return [0, 1].

### Example 2

**Input:**
```text
nums = [3, 2, 4], target = 6
```

**Output:**
```text
[1, 2]
```

**Explanation:**
Because nums[1] + nums[2] == 2 + 4 == 6, we return [1, 2].

### Example 3

**Input:**
```text
nums = [3, 3], target = 6
```

**Output:**
```text
[0, 1]
```

**Explanation:**
Because nums[0] + nums[1] == 3 + 3 == 6, we return [0, 1].

---

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
