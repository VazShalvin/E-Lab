# 9. Maximal Rectangle

**Topic**: Stack  
**Difficulty**: Hard  
**Tags**: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack

---

## Problem Statement

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return its area.

---

## Input & Output Format

- **Input**: A 2D character matrix `matrix` containing '0' and '1'.
- **Output**: An integer representing the maximal rectangle area.

---

## Sample Test Cases

### Example 1

**Input:**
```text
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
```

**Output:**
```text
6
```

**Explanation:**
The maximal rectangle has area = 6 (height 2, width 3).

### Example 2

**Input:**
```text
matrix = [["0"]]
```

**Output:**
```text
0
```

**Explanation:**
No '1' exists.

### Example 3

**Input:**
```text
matrix = [["1"]]
```

**Output:**
```text
1
```

**Explanation:**
Single cell '1' has area 1.

---

## Constraints

- `rows == matrix.length`, `cols == matrix[i].length`
- `1 <= row, cols <= 200`
- `matrix[i][j]` is `'0'` or `'1'`.

---

## Complexity Analysis

- **Time Complexity**: `O(R * C)`
- **Space Complexity**: `O(C)`
