# 12. Brick Wall

**Topic**: HashMap / Hashing  
**Difficulty**: Medium  
**Tags**: Array, Hash Table

---

## Problem Statement

There is a rectangular brick wall in front of you with `n` rows of bricks. The `i-th` row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the **least** number of bricks. If your line goes through the edge between two bricks, then the brick is not considered crossed. You cannot draw a line just along one of the two vertical edges of the wall.

Given the 2D array `wall`, return the minimum number of crossed bricks after drawing such a vertical line.

---

## Input & Output Format

- **Input**: A 2D integer array `wall`.
- **Output**: An integer representing minimum crossed bricks.

---

## Sample Test Cases

### Example 1

**Input:**
```text
wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
```

**Output:**
```text
2
```

**Explanation:**
Drawing line at position 4 intersects only 2 bricks.

### Example 2

**Input:**
```text
wall = [[1], [1], [1]]
```

**Output:**
```text
3
```

**Explanation:**
Cannot draw along external boundary, so line must cut through all 3 bricks.

### Example 3

**Input:**
```text
wall = [[1, 1], [2], [1, 1]]
```

**Output:**
```text
1
```

**Explanation:**
Line at position 1 cuts 1 brick (the second row).

---

## Constraints

- `n == wall.length`
- `1 <= n <= 10^4`
- `1 <= wall[i].length <= 10^4`
- `1 <= sum(wall[i].length) <= 2 * 10^4`
- `sum(wall[i])` is consistent across all rows.

---

## Complexity Analysis

- **Time Complexity**: `O(Total Bricks)`
- **Space Complexity**: `O(Number of Edges)`
