# 15. Partition to K Equal Sum Subsets

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if it is possible to divide this array into `k` non-empty subsets whose sums are all equal.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `k`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [4, 3, 2, 3, 5, 2, 1], k = 4
```

**Output:**
```text
true
```

**Explanation:**
Possible to divide into 4 subsets: (5), (1, 4), (2, 3), (2, 3) each summing to 5.

### Example 2

**Input:**
```text
nums = [1, 2, 3, 4], k = 3
```

**Output:**
```text
false
```

**Explanation:**
Total sum is 10, not divisible by 3.

### Example 3

**Input:**
```text
nums = [2, 2, 2, 2], k = 2
```

**Output:**
```text
true
```

**Explanation:**
Divide into [2, 2] and [2, 2].

---

## Constraints

- `1 <= k <= nums.length <= 16`
- `1 <= nums[i] <= 10^4`
- The frequency of each element is in the range `[1, 4]`.

---

## Complexity Analysis

- **Time Complexity**: `O(k * 2^N)`
- **Space Complexity**: `O(N)`
