# 12. Boats to Save People

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: Array, Two Pointers, Greedy, Sorting

---

## Problem Statement

You are given an array `people` where `people[i]` is the weight of the `i-th` person, and an **infinite number of boats** where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.

Return the minimum number of boats to carry every given person.

---

## Input & Output Format

- **Input**: An array of integers `people` and an integer `limit`.
- **Output**: An integer representing minimum boats.

---

## Sample Test Cases

### Example 1

**Input:**
```text
people = [1, 2], limit = 3
```

**Output:**
```text
1
```

**Explanation:**
1 boat (1, 2).

### Example 2

**Input:**
```text
people = [3, 2, 2, 1], limit = 3
```

**Output:**
```text
3
```

**Explanation:**
3 boats (1, 2), (2) and (3).

### Example 3

**Input:**
```text
people = [3, 5, 3, 4], limit = 5
```

**Output:**
```text
4
```

**Explanation:**
4 boats (3), (3), (4), (5).

---

## Constraints

- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= limit <= 3 * 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(1)`
