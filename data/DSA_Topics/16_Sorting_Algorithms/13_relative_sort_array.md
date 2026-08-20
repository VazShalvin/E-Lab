# 13. Relative Sort Array

**Topic**: Sorting Algorithms  
**Difficulty**: Easy  
**Tags**: Array, Hash Table, Sorting, Counting Sort

---

## Problem Statement

Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2` are also in `arr1`.

Sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in `arr2`. Elements that do not appear in `arr2` should be placed at the end of `arr1` in **ascending order**.

---

## Input & Output Format

- **Input**: Two arrays `arr1` and `arr2`.
- **Output**: Array `arr1` sorted relatively.

---

## Sample Test Cases

### Example 1

**Input:**
```text
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2 = [2, 1, 4, 3, 9, 6]
```

**Output:**
```text
[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
```

**Explanation:**
Elements present in arr2 are ordered as in arr2, followed by remaining [7, 19] in sorted order.

### Example 2

**Input:**
```text
arr1 = [28, 6, 22, 8, 44, 17], arr2 = [22, 28, 8, 6]
```

**Output:**
```text
[22, 28, 8, 6, 17, 44]
```

**Explanation:**
Relative sorted array.

### Example 3

**Input:**
```text
arr1 = [1], arr2 = [1]
```

**Output:**
```text
[1]
```

**Explanation:**
Single matching element.

---

## Constraints

- `1 <= arr1.length, arr2.length <= 1000`
- `0 <= arr1[i], arr2[i] <= 1000`
- All elements of `arr2` are distinct.

---

## Complexity Analysis

- **Time Complexity**: `O(N + M + K log K) or O(N + M) Counting Sort`
- **Space Complexity**: `O(1) (fixed 1001 count array)`
