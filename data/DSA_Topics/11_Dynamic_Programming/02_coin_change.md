# 2. Coin Change (Fewest Coins)

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: Array, Dynamic Programming, Breadth-First Search

---

## Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

---

## Input & Output Format

- **Input**: An array of integers `coins` and an integer `amount`.
- **Output**: An integer representing the minimum number of coins, or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
coins = [1, 2, 5], amount = 11
```

**Output:**
```text
3
```

**Explanation:**
11 = 5 + 5 + 1 (3 coins total).

### Example 2

**Input:**
```text
coins = [2], amount = 3
```

**Output:**
```text
-1
```

**Explanation:**
Cannot make amount 3 with only 2-cent coins.

### Example 3

**Input:**
```text
coins = [1], amount = 0
```

**Output:**
```text
0
```

**Explanation:**
0 coins needed for amount 0.

---

## Constraints

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(amount * len(coins))`
- **Space Complexity**: `O(amount)`
