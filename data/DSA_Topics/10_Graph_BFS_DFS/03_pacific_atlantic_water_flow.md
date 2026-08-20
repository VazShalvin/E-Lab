# 3. Pacific Atlantic Water Flow

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Array, Depth-First Search, Breadth-First Search, Matrix

---

## Problem Statement

There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

Water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height.

Return a 2D list of grid coordinates `result` where `result[i] = [r_i, c_i]` denotes that rain water can flow from cell `(r_i, c_i)` to **both** the Pacific and Atlantic oceans.

---

## Input & Output Format

- **Input**: A 2D integer matrix `heights`.
- **Output**: A list of coordinates `[[r, c], ...]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
```

**Output:**
```text
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
```

**Explanation:**
From each of these coordinates, water can drain into both oceans.

### Example 2

**Input:**
```text
heights = [[1]]
```

**Output:**
```text
[[0, 0]]
```

**Explanation:**
Single cell island connects to both oceans directly.

### Example 3

**Input:**
```text
heights = [[2, 1], [1, 2]]
```

**Output:**
```text
[[0, 0], [0, 1], [1, 0], [1, 2]]
```

**Explanation:**
All four cells can flow to both boundaries.

---

## Constraints

- `m == heights.length`, `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M * N)`
