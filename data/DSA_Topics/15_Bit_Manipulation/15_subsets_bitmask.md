# 15. Subsets Generation using Bitmask

**Topic**: Bit Manipulation  
**Difficulty**: Medium  
**Tags**: Array, Bit Manipulation

---

## Problem Statement

Given an integer array `nums` of unique elements, generate and return all possible subsets by iterating through all integer bitmasks from `0` to `2^n - 1`.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: A 2D array of subsets.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 3]
```

**Output:**
```text
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

**Explanation:**
Bitmask i from 0 (000b) to 7 (111b) encodes inclusion of nums[j] if ((i >> j) & 1).

### Example 2

**Input:**
```text
nums = [0]
```

**Output:**
```text
[[], [0]]
```

**Explanation:**
Bitmasks 0 and 1.

### Example 3

**Input:**
```text
nums = [5, 6]
```

**Output:**
```text
[[], [5], [6], [5, 6]]
```

**Explanation:**
4 bitmasks for length 2.

---

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All integers in `nums` are unique.

---

## Complexity Analysis

- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(1) auxiliary`
