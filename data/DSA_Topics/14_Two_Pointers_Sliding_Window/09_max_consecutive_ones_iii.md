# 9. Max Consecutive Ones III

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Array, Binary Search, Sliding Window, Prefix Sum

---

## Problem Statement

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

---

## Input & Output Format

- **Input**: A binary array `nums` and an integer `k`.
- **Output**: An integer representing the maximum consecutive 1s.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
```

**Output:**
```text
6
```

**Explanation:**
[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1] - bold numbers were flipped from 0 to 1. The longest subarray is 6.

### Example 2

**Input:**
```text
nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3
```

**Output:**
```text
10
```

**Explanation:**
Flipping 3 zeros gives a contiguous subarray of 10 ones.

### Example 3

**Input:**
```text
nums = [0, 0, 0], k = 1
```

**Output:**
```text
1
```

**Explanation:**
Flip one zero gives length 1.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
