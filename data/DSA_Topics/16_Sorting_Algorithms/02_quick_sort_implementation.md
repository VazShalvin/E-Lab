# 2. Quick Sort (3-Way Dutch Partitioning)

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, Divide and Conquer, Sorting, Two Pointers

---

## Problem Statement

Implement the Quick Sort algorithm to sort an array `nums` in ascending order using **3-way partitioning (Dutch National Flag pivot partitioning)** to handle duplicate values efficiently and prevent `O(N^2)` worst case degradation.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: Sorted array `nums`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [5, 2, 3, 1]
```

**Output:**
```text
[1, 2, 3, 5]
```

**Explanation:**
Ascending sorted array.

### Example 2

**Input:**
```text
nums = [5, 1, 1, 2, 0, 0]
```

**Output:**
```text
[0, 0, 1, 1, 2, 5]
```

**Explanation:**
Duplicates grouped and handled in O(N log N).

### Example 3

**Input:**
```text
nums = [1]
```

**Output:**
```text
[1]
```

**Explanation:**
Single element array.

---

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N) expected`
- **Space Complexity**: `O(log N) recursion stack`
