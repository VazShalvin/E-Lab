# 1. Kth Largest Element in an Array

**Topic**: Heap / Priority Queue  
**Difficulty**: Medium  
**Tags**: Array, Divide and Conquer, Sorting, Heap, Quickselect

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k-th` largest element in the array.

Note that it is the `k-th` largest element in the sorted order, not the `k-th` distinct element.

Can you solve it without sorting in `O(n)` average time?

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `k`.
- **Output**: An integer representing the `k-th` largest value.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [3, 2, 1, 5, 6, 4], k = 2
```

**Output:**
```text
5
```

**Explanation:**
Sorted order: [1, 2, 3, 4, 5, 6]. 2nd largest is 5.

### Example 2

**Input:**
```text
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
```

**Output:**
```text
4
```

**Explanation:**
Sorted order: [1, 2, 2, 3, 3, 4, 5, 5, 6]. 4th largest is 4.

### Example 3

**Input:**
```text
nums = [1], k = 1
```

**Output:**
```text
1
```

**Explanation:**
Single element is 1.

---

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N log k) using Min-Heap or O(N) Quickselect`
- **Space Complexity**: `O(k)`
