# 11. Sudoku Solver

**Topic**: Backtracking  
**Difficulty**: Hard  
**Tags**: Array, Hash Table, Backtracking, Matrix

---

## Problem Statement

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

---

## Input & Output Format

- **Input**: A 9x9 character matrix `board`.
- **Output**: Solved `board` in-place.

---

## Sample Test Cases

### Example 1

**Input:**
```text
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
```

**Output:**
```text
board filled completely satisfying all Sudoku rules.
```

**Explanation:**
Backtracking search fills cells adhering to row, col, box uniqueness.

### Example 2

**Input:**
```text
board with single empty cell
```

**Output:**
```text
Single missing digit placed.
```

**Explanation:**
Immediate deduction.

### Example 3

**Input:**
```text
Valid incomplete board
```

**Output:**
```text
Unique completed board.
```

**Explanation:**
Board guaranteed to have single unique solution.

---

## Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit or `'.'`. 
- It is guaranteed that the input board has only one solution.

---

## Complexity Analysis

- **Time Complexity**: `O(9^(empty_cells))`
- **Space Complexity**: `O(1) (fixed 81 stack)`
