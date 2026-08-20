# 2. Best Time to Buy and Sell Stock

**Topic**: Array  
**Difficulty**: Easy  
**Tags**: Array, Dynamic Programming

---

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

---

## Input & Output Format

- **Input**: An array of integers `prices`.
- **Output**: An integer representing maximum profit.

---

## Sample Test Cases

### Example 1

**Input:**
```text
prices = [7, 1, 5, 3, 6, 4]
```

**Output:**
```text
5
```

**Explanation:**
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

### Example 2

**Input:**
```text
prices = [7, 6, 4, 3, 1]
```

**Output:**
```text
0
```

**Explanation:**
In this case, no transactions are done and the max profit = 0.

### Example 3

**Input:**
```text
prices = [2, 4, 1]
```

**Output:**
```text
2
```

**Explanation:**
Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4 - 2 = 2.

---

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
