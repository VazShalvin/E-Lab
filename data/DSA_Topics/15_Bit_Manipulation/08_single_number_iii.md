# 8. Single Number III (Two elements appear once)

**Topic**: Bit Manipulation  
**Difficulty**: Medium  
**Tags**: Array, Bit Manipulation

---

## Problem Statement

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in **any order**.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An array of two integers `[val1, val2]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 1, 3, 2, 5]
```

**Output:**
```text
[3, 5]
```

**Explanation:**
[5, 3] is also a valid answer.

### Example 2

**Input:**
```text
nums = [-1, 0]
```

**Output:**
```text
[-1, 0]
```

**Explanation:**
Both elements appear once.

### Example 3

**Input:**
```text
nums = [0, 1]
```

**Output:**
```text
[1, 0]
```

**Explanation:**
Both appear once.

---

## Constraints

- `2 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each integer in `nums` will appear twice, only two integers will appear once.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
