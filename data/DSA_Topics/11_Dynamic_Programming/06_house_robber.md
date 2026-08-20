# 6. House Robber

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming

---

## Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight **without alerting the police**.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the maximum rob amount.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 3, 1]
```

**Output:**
```text
4
```

**Explanation:**
Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount = 1 + 3 = 4.

### Example 2

**Input:**
```text
nums = [2, 7, 9, 3, 1]
```

**Output:**
```text
12
```

**Explanation:**
Rob house 1 (money = 2), house 3 (money = 9) and house 5 (money = 1). Total amount = 2 + 9 + 1 = 12.

### Example 3

**Input:**
```text
nums = [2, 1, 1, 2]
```

**Output:**
```text
4
```

**Explanation:**
Rob house 0 (2) and house 3 (2) = 4.

---

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
