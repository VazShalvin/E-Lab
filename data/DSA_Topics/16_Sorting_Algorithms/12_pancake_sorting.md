# 12. Pancake Sorting

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, Two Pointers, Greedy, Sorting

---

## Problem Statement

Given an array of integers `arr`, sort the array by performing a series of **pancake flips**.

In one pancake flip we do the following steps:
- Choose an integer `k` where `1 <= k <= arr.length`.
- Reverse the sub-array `arr[0...k-1]` (0-indexed).

Return an array of the `k`-values corresponding to a sequence of pancake flips that sort `arr` within `10 * arr.length` flips.

---

## Input & Output Format

- **Input**: An array of integers `arr` containing permutations of 1 to n.
- **Output**: An array of `k` flip values.

---

## Sample Test Cases

### Example 1

**Input:**
```text
arr = [3, 2, 4, 1]
```

**Output:**
```text
[4, 2, 4, 3]
```

**Explanation:**
We perform 4 flips: k=4 -> [1, 4, 2, 3], k=2 -> [4, 1, 2, 3], k=4 -> [3, 2, 1, 4], k=3 -> [1, 2, 3, 4].

### Example 2

**Input:**
```text
arr = [1, 2, 3]
```

**Output:**
```text
[]
```

**Explanation:**
Already sorted, 0 flips.

### Example 3

**Input:**
```text
arr = [2, 1]
```

**Output:**
```text
[2]
```

**Explanation:**
k = 2 reverses to [1, 2].

---

## Constraints

- `1 <= arr.length <= 100`
- `1 <= arr[i] <= arr.length`
- All integers in `arr` are unique (i.e. `arr` is a permutation of integers from 1 to `arr.length`).

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`
