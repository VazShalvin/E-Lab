# 12. Find K Pairs with Smallest Sums

**Topic**: Heap / Priority Queue  
**Difficulty**: Medium  
**Tags**: Array, Heap

---

## Problem Statement

You are given two integer arrays `nums1` and `nums2` sorted in non-decreasing order and an integer `k`.

Define a pair `(u, v)` which consists of one element from `nums1` and one element from `nums2`.

Return the `k` pairs `(u_1, v_1), (u_2, v_2), ..., (u_k, v_k)` with the smallest sums.

---

## Input & Output Format

- **Input**: Two sorted arrays `nums1` and `nums2`, and an integer `k`.
- **Output**: A 2D array of `k` pairs `[[u_1, v_1], [u_2, v_2], ...]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3
```

**Output:**
```text
[[1, 2], [1, 4], [1, 6]]
```

**Explanation:**
Smallest sum pairs are [1, 2] (sum 3), [1, 4] (sum 5), [1, 6] (sum 7).

### Example 2

**Input:**
```text
nums1 = [1, 1, 2], nums2 = [1, 2, 3], k = 2
```

**Output:**
```text
[[1, 1], [1, 1]]
```

**Explanation:**
Pairs with smallest sum = 2.

### Example 3

**Input:**
```text
nums1 = [1, 2], nums2 = [3], k = 3
```

**Output:**
```text
[[1, 3], [2, 3]]
```

**Explanation:**
All possible pairs returned since k >= total pairs.

---

## Constraints

- `1 <= nums1.length, nums2.length <= 10^5`
- `-10^9 <= nums1[i], nums2[i] <= 10^9`
- `nums1` and `nums2` are sorted in non-decreasing order.
- `1 <= k <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(k log(min(N, k)))`
- **Space Complexity**: `O(min(N, k))`
