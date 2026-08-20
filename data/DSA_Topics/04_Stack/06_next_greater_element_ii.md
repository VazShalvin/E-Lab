# 6. Next Greater Element II (Circular Array)

**Topic**: Stack  
**Difficulty**: Medium  
**Tags**: Array, Stack, Monotonic Stack

---

## Problem Statement

Given a circular integer array `nums` (i.e., the next element of `nums[nums.length - 1]` is `nums[0]`), return the **next greater number** for every element in `nums`.

The next greater number of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `-1` for this number.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An array of integers representing the next greater element for each index.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 1]
```

**Output:**
```text
[2, -1, 2]
```

**Explanation:**
The first 1's next greater is 2; 2 has no greater; the second 1 searches circularly and finds 2.

### Example 2

**Input:**
```text
nums = [1, 2, 3, 4, 3]
```

**Output:**
```text
[2, 3, 4, -1, 4]
```

**Explanation:**
Circular search finds 4 for the last 3.

### Example 3

**Input:**
```text
nums = [5, 4, 3, 2, 1]
```

**Output:**
```text
[-1, 5, 5, 5, 5]
```

**Explanation:**
5 is maximum, rest find 5 circularly.

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
