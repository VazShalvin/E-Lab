# 10. N-Queens

**Topic**: Backtracking  
**Difficulty**: Hard  
**Tags**: Array, Backtracking

---

## Problem Statement

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the **n-queens puzzle**. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: A 2D array of string boards.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
[[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]]
```

**Explanation:**
There exist two distinct solutions to the 4-queens puzzle.

### Example 2

**Input:**
```text
n = 1
```

**Output:**
```text
[["Q"]]
```

**Explanation:**
Single queen on 1x1 board.

### Example 3

**Input:**
```text
n = 2
```

**Output:**
```text
[]
```

**Explanation:**
No valid solution exists for n = 2.

---

## Constraints

- `1 <= n <= 9`

---

## Complexity Analysis

- **Time Complexity**: `O(N!)`
- **Space Complexity**: `O(N)`
