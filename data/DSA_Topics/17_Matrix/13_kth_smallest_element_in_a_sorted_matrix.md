# 13. Kth Smallest Element in a Sorted Matrix

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Binary Search, Sorting, Heap, Matrix

---

## Problem Statement

Given an `n x n` `matrix` where each of the rows and columns is sorted in ascending order, return the `k-th` smallest element in the matrix.

Note that it is the `k-th` smallest element in the sorted order, not the `k-th` distinct element.

You must find a solution with a memory complexity better than `O(n^2)`.

---

## Input & Output Format

- **Input**: A 2D array `matrix` and an integer `k`.
- **Output**: An integer representing the `k-th` smallest element.

---

## Sample Test Cases

### Example 1

**Input:**
```text
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k = 8
```

**Output:**
```text
13
```

**Explanation:**
The elements in the matrix are [1, 5, 9, 10, 11, 12, 13, 13, 15], and the 8th smallest number is 13.

### Example 2

**Input:**
```text
matrix = [[-5]], k = 1
```

**Output:**
```text
-5
```

**Explanation:**
Single element matrix.

### Example 3

**Input:**
```text
matrix = [[1, 2], [1, 3]], k = 3
```

**Output:**
```text
2
```

**Explanation:**
3rd smallest is 2.

---

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All the rows and columns of `matrix` are **guaranteed** to be sorted in **non-decreasing order**.
- `1 <= k <= n^2`

---

## Complexity Analysis

- **Time Complexity**: `O(N * log(max - min)) with Binary Search`
- **Space Complexity**: `O(1)`
