# 6. Find Peak Element

**Topic**: Binary Search  
**Difficulty**: Medium  
**Tags**: Array, Binary Search

---

## Problem Statement

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`.

You must write an algorithm that runs in `O(log n)` time.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer index representing a peak element.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 3, 1]
```

**Output:**
```text
2
```

**Explanation:**
3 is a peak element and your function should return the index number 2.

### Example 2

**Input:**
```text
nums = [1, 2, 1, 3, 5, 6, 4]
```

**Output:**
```text
5
```

**Explanation:**
Your function can return index 1 (value 2) or index 5 (value 6).

### Example 3

**Input:**
```text
nums = [1]
```

**Output:**
```text
0
```

**Explanation:**
Index 0 is the peak element.

---

## Constraints

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
