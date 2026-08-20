# 9. Meeting Rooms II (Minimum Conference Rooms)

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, Two Pointers, Greedy, Sorting, Heap, Prefix Sum

---

## Problem Statement

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.

---

## Input & Output Format

- **Input**: A 2D array `intervals`.
- **Output**: An integer representing the minimum conference rooms.

---

## Sample Test Cases

### Example 1

**Input:**
```text
intervals = [[0, 30], [5, 10], [15, 20]]
```

**Output:**
```text
2
```

**Explanation:**
[0, 30] overlaps with [5, 10] and [15, 20], so at least 2 rooms are needed.

### Example 2

**Input:**
```text
intervals = [[7, 10], [2, 4]]
```

**Output:**
```text
1
```

**Explanation:**
No overlapping intervals, 1 room suffices.

### Example 3

**Input:**
```text
intervals = [[1, 5], [2, 6], [3, 7], [4, 8]]
```

**Output:**
```text
4
```

**Explanation:**
All 4 meetings overlap simultaneously at time 4.

---

## Constraints

- `1 <= intervals.length <= 10^4`
- `0 <= start_i < end_i <= 10^6`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
