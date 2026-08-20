# 7. Search Insert Position

**Topic**: Binary Search  
**Difficulty**: Easy  
**Tags**: Array, Binary Search

---

## Problem Statement

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

---

## Input & Output Format

- **Input**: Sorted array of integers `nums` and integer `target`.
- **Output**: An integer index.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 3, 5, 6], target = 5
```

**Output:**
```text
2
```

**Explanation:**
5 is found at index 2.

### Example 2

**Input:**
```text
nums = [1, 3, 5, 6], target = 2
```

**Output:**
```text
1
```

**Explanation:**
2 should be inserted at index 1.

### Example 3

**Input:**
```text
nums = [1, 3, 5, 6], target = 7
```

**Output:**
```text
4
```

**Explanation:**
7 should be inserted at the end (index 4).

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains distinct values sorted in ascending order.
- `-10^4 <= target <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
