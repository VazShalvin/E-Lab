# 1. Jump Game II (Minimum Jumps)

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Greedy

---

## Problem Statement

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`.

Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the minimum number of jumps.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [2, 3, 1, 1, 4]
```

**Output:**
```text
2
```

**Explanation:**
The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

### Example 2

**Input:**
```text
nums = [2, 3, 0, 1, 4]
```

**Output:**
```text
2
```

**Explanation:**
Jump 0 -> 1 -> 4 takes 2 jumps.

### Example 3

**Input:**
```text
nums = [1, 1, 1, 1]
```

**Output:**
```text
3
```

**Explanation:**
1 jump per step.

---

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
