# 10. Surrounded Regions (Capture Border-free O's)

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

---

## Problem Statement

Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally **surrounded by** `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region. An `'O'` is not captured if it is on the boundary or connected to an `'O'` on the boundary.

---

## Input & Output Format

- **Input**: A 2D character matrix `board`.
- **Output**: Modified `board` in-place.

---

## Sample Test Cases

### Example 1

**Input:**
```text
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
```

**Output:**
```text
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
```

**Explanation:**
Surrounded 'O's in the interior are flipped to 'X'. The 'O' at board[3][1] is on the boundary and remains 'O'.

### Example 2

**Input:**
```text
board = [["X"]]
```

**Output:**
```text
[["X"]]
```

**Explanation:**
No 'O' to capture.

### Example 3

**Input:**
```text
board = [["O","O"],["O","O"]]
```

**Output:**
```text
[["O","O"],["O","O"]]
```

**Explanation:**
All 'O's touch boundaries, so none are flipped.

---

## Constraints

- `m == board.length`, `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M * N)`
