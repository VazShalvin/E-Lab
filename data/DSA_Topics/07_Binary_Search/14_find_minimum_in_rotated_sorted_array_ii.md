# 14. Find Minimum in Rotated Sorted Array II (With Duplicates)

**Topic**: Binary Search  
**Difficulty**: Hard  
**Tags**: Array, Binary Search

---

## Problem Statement

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. The array may contain **duplicates**.

Given the sorted rotated array `nums`, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the minimum element.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 3, 5]
```

**Output:**
```text
1
```

**Explanation:**
Array has not been rotated or min is at index 0.

### Example 2

**Input:**
```text
nums = [2, 2, 2, 0, 1]
```

**Output:**
```text
0
```

**Explanation:**
Minimum value 0 is located at index 3.

### Example 3

**Input:**
```text
nums = [3, 3, 1, 3]
```

**Output:**
```text
1
```

**Explanation:**
Handles duplicate edges cleanly by decrementing high pointer.

---

## Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- `nums` is sorted and rotated.

---

## Complexity Analysis

- **Time Complexity**: `O(log N) average, O(N) worst case`
- **Space Complexity**: `O(1)`
