# 3. Contains Duplicate

**Topic**: Array  
**Difficulty**: Easy  
**Tags**: Array, Hash Table, Sorting

---

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 3, 1]
```

**Output:**
```text
true
```

**Explanation:**
1 appears at index 0 and index 3.

### Example 2

**Input:**
```text
nums = [1, 2, 3, 4]
```

**Output:**
```text
false
```

**Explanation:**
All elements are distinct.

### Example 3

**Input:**
```text
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
```

**Output:**
```text
true
```

**Explanation:**
Multiple duplicates exist (1, 3, 4, 2).

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
