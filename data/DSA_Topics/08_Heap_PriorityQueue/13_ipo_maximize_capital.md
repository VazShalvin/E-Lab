# 13. IPO (Maximize Capital)

**Topic**: Heap / Priority Queue  
**Difficulty**: Hard  
**Tags**: Array, Greedy, Sorting, Heap

---

## Problem Statement

Suppose LeetCode will start its IPO soon. To sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO.

You are given `n` projects where the `i-th` project has a pure profit `profits[i]` and a minimum capital of `capital[i]` is needed to start it.

Initially, you have `w` capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of **at most `k` distinct projects** from given projects to **maximize your eventual capital**, and return the final maximized capital.

---

## Input & Output Format

- **Input**: An integer `k`, initial capital `w`, and integer arrays `profits` and `capital`.
- **Output**: An integer representing maximized capital.

---

## Sample Test Cases

### Example 1

**Input:**
```text
k = 2, w = 0, profits = [1, 2, 3], capital = [0, 1, 1]
```

**Output:**
```text
4
```

**Explanation:**
With w = 0, can only start project 0 (profit 1) -> w becomes 1. Then start project 2 (capital 1, profit 3) -> w becomes 4.

### Example 2

**Input:**
```text
k = 3, w = 0, profits = [1, 2, 3], capital = [0, 1, 2]
```

**Output:**
```text
6
```

**Explanation:**
Start projects in order 0 -> 1 -> 2: 0 + 1 + 2 + 3 = 6.

### Example 3

**Input:**
```text
k = 1, w = 2, profits = [1, 2, 3], capital = [1, 1, 2]
```

**Output:**
```text
5
```

**Explanation:**
Pick highest profit project 2: 2 + 3 = 5.

---

## Constraints

- `1 <= k <= 10^5`
- `0 <= w <= 10^9`
- `n == profits.length == capital.length`
- `1 <= n <= 10^5`
- `0 <= profits[i] <= 10^4`
- `0 <= capital[i] <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N + k log N)`
- **Space Complexity**: `O(N)`
