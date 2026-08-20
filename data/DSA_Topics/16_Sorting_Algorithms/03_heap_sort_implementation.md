# 3. Heap Sort In-Place Implementation

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, Sorting, Heap

---

## Problem Statement

Implement the Heap Sort algorithm to sort an array `nums` in-place using a **Max-Heap** with `O(1)` auxiliary space.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: Sorted array `nums`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [12, 11, 13, 5, 6, 7]
```

**Output:**
```text
[5, 6, 7, 11, 12, 13]
```

**Explanation:**
Build max heap then repeatedly extract max to back.

### Example 2

**Input:**
```text
nums = [4, 10, 3, 5, 1]
```

**Output:**
```text
[1, 3, 4, 5, 10]
```

**Explanation:**
In-place sorted array.

### Example 3

**Input:**
```text
nums = [1, 2, 3]
```

**Output:**
```text
[1, 2, 3]
```

**Explanation:**
Preserves sorted order.

---

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-10^5 <= nums[i] <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(1)`
