# 7. Word Search

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: Array, String, Backtracking, Matrix

---

## Problem Statement

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

---

## Input & Output Format

- **Input**: A 2D character matrix `board` and a string `word`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
```

**Output:**
```text
true
```

**Explanation:**
Path: (0,0)->(0,1)->(0,2)->(1,2)->(2,2)->(2,1).

### Example 2

**Input:**
```text
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
```

**Output:**
```text
true
```

**Explanation:**
Path: (1,3)->(2,3)->(2,2).

### Example 3

**Input:**
```text
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
```

**Output:**
```text
false
```

**Explanation:**
Cannot reuse cell (0,1).

---

## Constraints

- `m == board.length`, `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consist of only lowercase and uppercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N * 3^L) where L is word length`
- **Space Complexity**: `O(L)`
