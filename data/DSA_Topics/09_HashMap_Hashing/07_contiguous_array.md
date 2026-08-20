# 7. Contiguous Array (Equal 0s and 1s)

**Topic**: HashMap / Hashing  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Prefix Sum

---

## Problem Statement

Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of `0` and `1`.

---

## Input & Output Format

- **Input**: An array of binary integers `nums`.
- **Output**: An integer representing the maximum length.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [0, 1]
```

**Output:**
```text
2
```

**Explanation:**
[0, 1] has an equal number of zeroes and ones.

### Example 2

**Input:**
```text
nums = [0, 1, 0]
```

**Output:**
```text
2
```

**Explanation:**
[0, 1] or [1, 0] is the longest with equal 0 and 1.

### Example 3

**Input:**
```text
nums = [0, 0, 1, 0, 0, 0, 1, 1]
```

**Output:**
```text
6
```

**Explanation:**
Subarray [1, 0, 0, 0, 1, 1] or [0, 1, 0, 0, 1, 1] has length 6 with three 0s and three 1s.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
