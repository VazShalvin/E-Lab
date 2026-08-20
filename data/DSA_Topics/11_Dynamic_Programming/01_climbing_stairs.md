# 1. Climbing Stairs

**Topic**: Dynamic Programming  
**Difficulty**: Easy  
**Tags**: Math, Dynamic Programming, Memoization

---

## Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: An integer representing the distinct number of ways.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 2
```

**Output:**
```text
2
```

**Explanation:**
There are two ways to climb to the top:
1. 1 step + 1 step
2. 2 steps

### Example 2

**Input:**
```text
n = 3
```

**Output:**
```text
3
```

**Explanation:**
Three ways:
1. 1 + 1 + 1
2. 1 + 2
3. 2 + 1

### Example 3

**Input:**
```text
n = 5
```

**Output:**
```text
8
```

**Explanation:**
Fibonacci sequence: dp[5] = 8.

---

## Constraints

- `1 <= n <= 45`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
