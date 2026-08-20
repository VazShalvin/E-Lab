# 5. Next Greater Element I

**Topic**: Stack  
**Difficulty**: Easy  
**Tags**: Array, Hash Table, Stack, Monotonic Stack

---

## Problem Statement

The **next greater element** of some element `x` in an array is the first greater element that is to the right of `x` in the same array.

You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element as described above.

---

## Input & Output Format

- **Input**: Two arrays `nums1` and `nums2`.
- **Output**: An array of integers `ans`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
```

**Output:**
```text
[-1, 3, -1]
```

**Explanation:**
For 4 in nums2, no greater element to right -> -1.
For 1 in nums2, next greater is 3.
For 2 in nums2, no greater element to right -> -1.

### Example 2

**Input:**
```text
nums1 = [2, 4], nums2 = [1, 2, 3, 4]
```

**Output:**
```text
[3, -1]
```

**Explanation:**
For 2 in nums2, next greater is 3.
For 4 in nums2, no greater element -> -1.

### Example 3

**Input:**
```text
nums1 = [1, 3, 5, 2, 4], nums2 = [6, 5, 4, 3, 2, 1, 7]
```

**Output:**
```text
[7, 7, 7, 7, 7]
```

**Explanation:**
All elements find 7 as next greater element.

---

## Constraints

- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 10^4`
- All integers in `nums1` and `nums2` are unique.
- All the integers of `nums1` also appear in `nums2`.

---

## Complexity Analysis

- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(M)`
