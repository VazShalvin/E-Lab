# 9. Unique Paths

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: Math, Dynamic Programming, Combinatorics

---

## Problem Statement

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

---

## Input & Output Format

- **Input**: Two integers `m` and `n`.
- **Output**: An integer representing the number of paths.

---

## Sample Test Cases

### Example 1

**Input:**
```text
m = 3, n = 7
```

**Output:**
```text
28
```

**Explanation:**
From (0,0) to (2,6) there are 28 unique ways.

### Example 2

**Input:**
```text
m = 3, n = 2
```

**Output:**
```text
3
```

**Explanation:**
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

### Example 3

**Input:**
```text
m = 1, n = 1
```

**Output:**
```text
1
```

**Explanation:**
Already at destination, 1 path.

---

## Constraints

- `1 <= m, n <= 100`

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(N)`
