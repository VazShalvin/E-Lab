# 9. Predict the Winner (Minimax Recursion)

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: Array, Math, Dynamic Programming, Recursion, Game Theory

---

## Problem Statement

You are given an integer array `nums`. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of `0`. At each turn, the player takes one of the numbers from either end of the array (i.e., `nums[0]` or `nums[nums.length - 1]`) which reduces the size of the array by `1`. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return `true` if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return `true`.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 5, 2]
```

**Output:**
```text
false
```

**Explanation:**
Initially, player 1 can choose between 1 and 2. If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. Player 2 wins.

### Example 2

**Input:**
```text
nums = [1, 5, 233, 7]
```

**Output:**
```text
true
```

**Explanation:**
Player 1 can pick 1 first, then either 233 or 7 to secure winning score.

### Example 3

**Input:**
```text
nums = [1, 1]
```

**Output:**
```text
true
```

**Explanation:**
Tied score 1-1, Player 1 wins by rule.

---

## Constraints

- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 10^7`

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`
