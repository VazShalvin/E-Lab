# 13. Interval List Intersections

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Array, Two Pointers

---

## Problem Statement

You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [start_i, end_i]` and `secondList[j] = [start_j, end_j]`. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

---

## Input & Output Format

- **Input**: Two 2D arrays `firstList` and `secondList`.
- **Output**: A 2D array representing intersection intervals.

---

## Sample Test Cases

### Example 1

**Input:**
```text
firstList = [[0, 2], [5, 10], [13, 23], [24, 25]], secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
```

**Output:**
```text
[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
```

**Explanation:**
Overlapping intervals computed using two pointers.

### Example 2

**Input:**
```text
firstList = [[1, 3], [5, 9]], secondList = []
```

**Output:**
```text
[]
```

**Explanation:**
Empty list intersection is empty.

### Example 3

**Input:**
```text
firstList = [[1, 7]], secondList = [[3, 10]]
```

**Output:**
```text
[[3, 7]]
```

**Explanation:**
Intersection is [max(1, 3), min(7, 10)] = [3, 7].

---

## Constraints

- `0 <= firstList.length, secondList.length <= 1000`
- `firstList[i].length == 2`, `secondList[j].length == 2`
- `0 <= start_i < end_i <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
