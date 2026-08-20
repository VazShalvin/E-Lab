# 7. Single Number II (Every other element appears 3 times)

**Topic**: Bit Manipulation  
**Difficulty**: Medium  
**Tags**: Array, Bit Manipulation

---

## Problem Statement

Given an integer array `nums` where every element appears **three times** except for one, which appears **exactly once**. Find the single element and return it.

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
nums = [2, 2, 3, 2]
```

**Output:**
```text
3
```

**Explanation:**
3 appears once, while 2 appears three times.

### Example 2

**Input:**
```text
nums = [0, 1, 0, 1, 0, 1, 99]
```

**Output:**
```text
99
```

**Explanation:**
99 appears once.

### Example 3

**Input:**
```text
nums = [7, 7, 7, 4]
```

**Output:**
```text
4
```

**Explanation:**
4 is the single element.

---

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each element in `nums` appears exactly three times except for one element which appears once.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
