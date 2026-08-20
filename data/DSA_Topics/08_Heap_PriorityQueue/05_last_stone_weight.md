# 5. Last Stone Weight

**Topic**: Heap / Priority Queue  
**Difficulty**: Easy  
**Tags**: Array, Heap

---

## Problem Statement

You are given an array of integers `stones` where `stones[i]` is the weight of the `i-th` stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones with weights `x` and `y` with `x <= y`. The result of this smash is:
- If `x == y`, both stones are destroyed.
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is at most one stone left. Return the weight of the last remaining stone. If there are no stones left, return `0`.

---

## Input & Output Format

- **Input**: An array of integers `stones`.
- **Output**: An integer representing the last stone's weight.

---

## Sample Test Cases

### Example 1

**Input:**
```text
stones = [2, 7, 4, 1, 8, 1]
```

**Output:**
```text
1
```

**Explanation:**
We combine 7 and 8 to get 1 so the array converts to [2, 4, 1, 1, 1] then, we combine 2 and 4 to get 2 so [2, 1, 1, 1] then, we combine 2 and 1 to get 1 so [1, 1, 1] then, we combine 1 and 1 to get 0 so [1] then that's the value of the last stone.

### Example 2

**Input:**
```text
stones = [1]
```

**Output:**
```text
1
```

**Explanation:**
Single stone remains 1.

### Example 3

**Input:**
```text
stones = [2, 2]
```

**Output:**
```text
0
```

**Explanation:**
Both stones destroy each other.

---

## Constraints

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
