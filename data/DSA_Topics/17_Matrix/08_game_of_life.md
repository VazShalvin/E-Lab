# 8. Game of Life (Conway's Simulation In-Place)

**Topic**: Matrix  
**Difficulty**: Medium  
**Tags**: Array, Matrix, Simulation

---

## Problem Statement

According to Wikipedia's article: "The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: live (represented by a `1`) or dead (represented by a `0`). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:
1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

Update the board in-place with `O(1)` extra space.

---

## Input & Output Format

- **Input**: A 2D integer matrix `board`.
- **Output**: Updated `board` in-place.

---

## Sample Test Cases

### Example 1

**Input:**
```text
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
```

**Output:**
```text
[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
```

**Explanation:**
Simulates 1 time step using 2-bit state encoding.

### Example 2

**Input:**
```text
board = [[1, 1], [1, 0]]
```

**Output:**
```text
[[1, 1], [1, 1]]
```

**Explanation:**
Dead cell (1, 1) has 3 live neighbors and reproduces.

### Example 3

**Input:**
```text
board = [[0]]
```

**Output:**
```text
[[0]]
```

**Explanation:**
Single dead cell remains dead.

---

## Constraints

- `m == board.length`, `n == board[i].length`
- `1 <= m, n <= 25`
- `board[i][j]` is `0` or `1`.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(1)`
