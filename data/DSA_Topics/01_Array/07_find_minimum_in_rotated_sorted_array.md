# 7. Find Minimum in Rotated Sorted Array

**Topic**: Array  
**Difficulty**: Medium  
**Tags**: Array, Binary Search

---

## Problem Statement

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the minimum element.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [3, 4, 5, 1, 2]
```

**Output:**
```text
1
```

**Explanation:**
Original array was [1, 2, 3, 4, 5] rotated 3 times.

### Example 2

**Input:**
```text
nums = [4, 5, 6, 7, 0, 1, 2]
```

**Output:**
```text
0
```

**Explanation:**
Original array was [0, 1, 2, 4, 5, 6, 7] and it was rotated 4 times.

### Example 3

**Input:**
```text
nums = [11, 13, 15, 17]
```

**Output:**
```text
11
```

**Explanation:**
Original array was rotated 4 times (identical to 0 rotations).

---

## Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are unique.

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
