# 8. Maximum Subsequence Score

**Topic**: Heap / Priority Queue  
**Difficulty**: Medium  
**Tags**: Array, Greedy, Sorting, Heap

---

## Problem Statement

You are given two **0-indexed** integer arrays `nums1` and `nums2` of equal length `n` and a positive integer `k`. You must choose a subsequence of indices from `nums1` of length `k`.

For chosen indices `i_0, i_1, ..., i_k-1`, your score is defined as:
`Score = (nums1[i_0] + nums1[i_1] + ... + nums1[i_k-1]) * min(nums2[i_0], nums2[i_1], ..., nums2[i_k-1])`

Return the **maximum** possible score.

---

## Input & Output Format

- **Input**: Two arrays `nums1`, `nums2`, and an integer `k`.
- **Output**: An integer (64-bit) representing the maximum score.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums1 = [1, 3, 3, 2], nums2 = [2, 1, 3, 4], k = 3
```

**Output:**
```text
12
```

**Explanation:**
Choosing indices 0, 2, 3 gives sum = 1 + 3 + 2 = 6, and min(2, 3, 4) = 2. Score = 6 * 2 = 12.

### Example 2

**Input:**
```text
nums1 = [4, 2, 3, 1, 1], nums2 = [7, 5, 10, 9, 6], k = 1
```

**Output:**
```text
30
```

**Explanation:**
Index 2 gives sum = 3, min = 10, score = 3 * 10 = 30.

### Example 3

**Input:**
```text
nums1 = [2, 1, 14, 12], nums2 = [11, 7, 13, 6], k = 2
```

**Output:**
```text
168
```

**Explanation:**
Indices 2, 3 give (14 + 12) * min(13, 6) = 26 * 6 = 156 or indices 0, 2 give (2 + 14) * 11 = 176.

---

## Constraints

- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i] <= 10^5`
- `1 <= nums2[i] <= 10^5`
- `1 <= k <= n`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
