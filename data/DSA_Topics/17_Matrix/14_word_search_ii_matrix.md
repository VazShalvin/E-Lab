# 14. Word Search II (Trie + Matrix DFS)

**Topic**: Matrix  
**Difficulty**: Hard  
**Tags**: Array, String, Backtracking, Trie, Matrix

---

## Problem Statement

Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

---

## Input & Output Format

- **Input**: A 2D character matrix `board` and an array of strings `words`.
- **Output**: A list of strings found on the board.

---

## Sample Test Cases

### Example 1

**Input:**
```text
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
```

**Output:**
```text
["eat", "oath"]
```

**Explanation:**
"eat" and "oath" are formed by connected paths.

### Example 2

**Input:**
```text
board = [["a","b"],["c","d"]], words = ["abcb"]
```

**Output:**
```text
[]
```

**Explanation:**
Cannot reuse cell 'b'.

### Example 3

**Input:**
```text
board = [["a"]], words = ["a"]
```

**Output:**
```text
["a"]
```

**Explanation:**
Single letter word matched.

---

## Constraints

- `m == board.length`, `n == board[i].length`
- `1 <= m, n <= 12`
- `1 <= words.length <= 3 * 10^4`
- `1 <= words[i].length <= 10`
- `board` and `words[i]` consist of lowercase English letters.
- All strings of `words` are unique.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N * 3^(L-1))`
- **Space Complexity**: `O(Total Characters in Words)`
