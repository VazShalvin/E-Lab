# 1. Two Sum II - Input Array Is Sorted

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Array, Two Pointers, Binary Search

---

## Problem Statement

Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

---

## Input & Output Format

- **Input**: A sorted array of integers `numbers` and an integer `target`.
- **Output**: An array of two 1-indexed integers `[index1, index2]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
numbers = [2, 7, 11, 15], target = 9
```

**Output:**
```text
[1, 2]
```

**Explanation:**
The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

### Example 2

**Input:**
```text
numbers = [2, 3, 4], target = 6
```

**Output:**
```text
[1, 3]
```

**Explanation:**
2 + 4 = 6. index1 = 1, index2 = 3.

### Example 3

**Input:**
```text
numbers = [-1, 0], target = -1
```

**Output:**
```text
[1, 2]
```

**Explanation:**
(-1) + 0 = -1. index1 = 1, index2 = 2.

---

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- Exactly one valid answer exists.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
