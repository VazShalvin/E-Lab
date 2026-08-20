# 12. Insert Interval

**Topic**: Array  
**Difficulty**: Medium  
**Tags**: Array

---

## Problem Statement

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

---

## Input & Output Format

- **Input**: A 2D array `intervals` and a 1D array `newInterval`.
- **Output**: A 2D array of merged non-overlapping intervals.

---

## Sample Test Cases

### Example 1

**Input:**
```text
intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
```

**Output:**
```text
[[1, 5], [6, 9]]
```

**Explanation:**
newInterval [2, 5] overlaps with [1, 3], merging to [1, 5].

### Example 2

**Input:**
```text
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
```

**Output:**
```text
[[1, 2], [3, 10], [12, 16]]
```

**Explanation:**
Because the new interval [4, 8] overlaps with [3, 5], [6, 7], [8, 10].

### Example 3

**Input:**
```text
intervals = [], newInterval = [5, 7]
```

**Output:**
```text
[[5, 7]]
```

**Explanation:**
Inserting into an empty list returns the interval itself.

---

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in ascending order.
- `newInterval.length == 2`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
