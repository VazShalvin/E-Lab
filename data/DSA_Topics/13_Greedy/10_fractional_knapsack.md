# 10. Fractional Knapsack Problem

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: Greedy, Sorting

---

## Problem Statement

Given weights and values of `N` items, we need to put these items in a knapsack of capacity `W` to get the **maximum total value** in the knapsack. In Fractional Knapsack, we can break items for maximizing the total value of knapsack.

---

## Input & Output Format

- **Input**: An integer `W` (capacity), and two arrays `values` and `weights`.
- **Output**: A double representing maximum total value.

---

## Sample Test Cases

### Example 1

**Input:**
```text
W = 50, values = [60, 100, 120], weights = [10, 20, 30]
```

**Output:**
```text
240.000000
```

**Explanation:**
Take item 1 (value 60, weight 10), item 2 (value 100, weight 20), and 2/3 of item 3 (value 80, weight 20). Total = 60 + 100 + 80 = 240.

### Example 2

**Input:**
```text
W = 10, values = [500], weights = [30]
```

**Output:**
```text
166.666667
```

**Explanation:**
Take 10/30 of the item: 500 * (10/30) = 166.67.

### Example 3

**Input:**
```text
W = 10, values = [10, 20], weights = [5, 5]
```

**Output:**
```text
30.000000
```

**Explanation:**
Take both items completely: 10 + 20 = 30.

---

## Constraints

- `1 <= N <= 10^5`
- `1 <= W <= 10^9`
- `1 <= values[i], weights[i] <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
