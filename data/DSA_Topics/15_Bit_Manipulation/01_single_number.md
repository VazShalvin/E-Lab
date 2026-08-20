# 1. Single Number

**Topic**: Bit Manipulation  
**Difficulty**: Easy  
**Tags**: Array, Bit Manipulation

---

## Problem Statement

Given a **non-empty** array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the unique element.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [2, 2, 1]
```

**Output:**
```text
1
```

**Explanation:**
XORing all elements: 2 ^ 2 ^ 1 = 0 ^ 1 = 1.

### Example 2

**Input:**
```text
nums = [4, 1, 2, 1, 2]
```

**Output:**
```text
4
```

**Explanation:**
4 is the only number appearing once.

### Example 3

**Input:**
```text
nums = [1]
```

**Output:**
```text
1
```

**Explanation:**
Single element is 1.

---

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element appears twice except for one.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
