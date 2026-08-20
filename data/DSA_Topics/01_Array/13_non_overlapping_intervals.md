# 13. Non-overlapping Intervals

**Topic**: Array  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Greedy, Sorting

---

## Problem Statement

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

---

## Input & Output Format

- **Input**: A 2D array `intervals`.
- **Output**: An integer representing the minimum number of removals.

---

## Sample Test Cases

### Example 1

**Input:**
```text
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
```

**Output:**
```text
1
```

**Explanation:**
[1, 3] can be removed and the rest of the intervals are non-overlapping.

### Example 2

**Input:**
```text
intervals = [[1, 2], [1, 2], [1, 2]]
```

**Output:**
```text
2
```

**Explanation:**
You need to remove two [1, 2] to make the rest of the intervals non-overlapping.

### Example 3

**Input:**
```text
intervals = [[1, 2], [2, 3]]
```

**Output:**
```text
0
```

**Explanation:**
You don't need to remove any of the intervals since they're already non-overlapping.

---

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(1)`
