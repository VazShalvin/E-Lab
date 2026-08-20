# 13. Two City Scheduling

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: Array, Greedy, Sorting

---

## Problem Statement

A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCost_i, bCost_i]`, the cost of flying the `i-th` person to city `a` is `aCost_i`, and the cost of flying the `i-th` person to city `b` is `bCost_i`.

Return the minimum cost to fly every person to a city such that exactly `n` people arrive in each city.

---

## Input & Output Format

- **Input**: A 2D array `costs`.
- **Output**: An integer representing minimum total cost.

---

## Sample Test Cases

### Example 1

**Input:**
```text
costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
```

**Output:**
```text
110
```

**Explanation:**
Send person 0 to A (10), person 1 to A (30), person 2 to B (50), person 3 to B (20). Total = 10 + 30 + 50 + 20 = 110.

### Example 2

**Input:**
```text
costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
```

**Output:**
```text
1859
```

**Explanation:**
Optimal assignment minimizes cost difference.

### Example 3

**Input:**
```text
costs = [[1, 2], [3, 4]]
```

**Output:**
```text
5
```

**Explanation:**
1 to A, 4 to B = 5.

---

## Constraints

- `2 * n == costs.length`
- `2 <= costs.length <= 100`
- `costs.length` is even.
- `1 <= aCost_i, bCost_i <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(1)`
