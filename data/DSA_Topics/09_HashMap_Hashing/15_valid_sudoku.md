# 15. Valid Sudoku

**Topic**: HashMap / Hashing  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Matrix

---

## Problem Statement

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.

---

## Input & Output Format

- **Input**: A 9x9 2D character array `board`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
```

**Output:**
```text
true
```

**Explanation:**
All rows, columns, and 3x3 boxes satisfy Sudoku constraints without duplication.

### Example 2

**Input:**
```text
board = same as above but with board[0][0] = "8"
```

**Output:**
```text
false
```

**Explanation:**
Row 0 and column 0 already contain "8" in board[3][0], violating duplicate constraint.

### Example 3

**Input:**
```text
board with all "."
```

**Output:**
```text
true
```

**Explanation:**
Empty board is valid.

---

## Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `'1'-'9'` or `'.'`. 

---

## Complexity Analysis

- **Time Complexity**: `O(1) (fixed 81 cells)`
- **Space Complexity**: `O(1)`
