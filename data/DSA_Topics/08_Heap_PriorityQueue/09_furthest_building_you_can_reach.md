# 9. Furthest Building You Can Reach

**Topic**: Heap / Priority Queue  
**Difficulty**: Medium  
**Tags**: Array, Greedy, Heap

---

## Problem Statement

You are given an integer array `heights` representing the heights of buildings, some `bricks`, and some `ladders`.

You start your journey from building `0` and move to the next building by possibly using bricks or ladders.

While moving from building `i` to building `i+1` (0-indexed):
- If the current building's height is greater than or equal to the next building's height, you do **not** need a ladder or bricks.
- If the current building's height is less than the next building's height, you can either use **one ladder** or `(h[i+1] - h[i])` **bricks**.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

---

## Input & Output Format

- **Input**: An array of integers `heights`, and integers `bricks` and `ladders`.
- **Output**: An integer index.

---

## Sample Test Cases

### Example 1

**Input:**
```text
heights = [4, 2, 7, 6, 9, 14, 12], bricks = 5, ladders = 1
```

**Output:**
```text
4
```

**Explanation:**
Go to 1 (cost 0), go to 2 (use 5 bricks), go to 3 (cost 0), go to 4 (use 1 ladder). Cannot reach 5.

### Example 2

**Input:**
```text
heights = [4, 12, 2, 7, 3, 18, 20, 3, 19], bricks = 10, ladders = 2
```

**Output:**
```text
7
```

**Explanation:**
Reach building index 7 optimally.

### Example 3

**Input:**
```text
heights = [14, 3, 19, 3], bricks = 17, ladders = 0
```

**Output:**
```text
3
```

**Explanation:**
Use 16 bricks to jump to building 2, then reach 3 without cost.

---

## Constraints

- `1 <= heights.length <= 10^5`
- `1 <= heights[i] <= 10^6`
- `0 <= bricks <= 10^9`
- `0 <= ladders <= heights.length`

---

## Complexity Analysis

- **Time Complexity**: `O(N log(ladders))`
- **Space Complexity**: `O(ladders)`
