# 11. Single Element in a Sorted Array

**Topic**: Binary Search  
**Difficulty**: Medium  
**Tags**: Array, Binary Search

---

## Problem Statement

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in `O(log n)` time and `O(1)` space.

---

## Input & Output Format

- **Input**: A sorted array of integers `nums`.
- **Output**: An integer representing the unique element.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
```

**Output:**
```text
2
```

**Explanation:**
2 appears only once.

### Example 2

**Input:**
```text
nums = [3, 3, 7, 7, 10, 11, 11]
```

**Output:**
```text
10
```

**Explanation:**
10 appears only once.

### Example 3

**Input:**
```text
nums = [1]
```

**Output:**
```text
1
```

**Explanation:**
1 is the single element.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
