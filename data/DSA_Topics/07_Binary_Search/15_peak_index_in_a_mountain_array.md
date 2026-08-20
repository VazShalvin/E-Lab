# 15. Peak Index in a Mountain Array

**Topic**: Binary Search  
**Difficulty**: Medium  
**Tags**: Array, Binary Search

---

## Problem Statement

An array `arr` is a mountain if the following properties hold:
- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given a mountain array `arr`, return the index `i` such that `arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`.

You must solve it in `O(log(arr.length))` time complexity.

---

## Input & Output Format

- **Input**: An array of integers `arr`.
- **Output**: An integer representing the peak index.

---

## Sample Test Cases

### Example 1

**Input:**
```text
arr = [0, 1, 0]
```

**Output:**
```text
1
```

**Explanation:**
Peak is at index 1.

### Example 2

**Input:**
```text
arr = [0, 2, 1, 0]
```

**Output:**
```text
1
```

**Explanation:**
Peak is at index 1.

### Example 3

**Input:**
```text
arr = [0, 10, 5, 2]
```

**Output:**
```text
1
```

**Explanation:**
Peak is at index 1 with value 10.

---

## Constraints

- `3 <= arr.length <= 10^5`
- `0 <= arr[i] <= 10^6`
- `arr` is guaranteed to be a mountain array.

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
