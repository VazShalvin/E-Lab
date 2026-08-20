# 14. Find the Winner of the Circular Game (Josephus Problem)

**Topic**: Queue  
**Difficulty**: Medium  
**Tags**: Array, Math, Recursion, Queue, Simulation

---

## Problem Statement

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in clockwise order.

The rules of the game are as follows:
1. Start at the 1st friend.
2. Count the next `k` friends in the clockwise direction including the friend you started at. The counting wraps around the circle.
3. The last friend you counted leaves the circle and loses the game.
4. If there is still more than one friend in the circle, repeat from the next friend.

Given the number of friends, `n`, and an integer `k`, return the winner of the game.

---

## Input & Output Format

- **Input**: Two integers `n` and `k`.
- **Output**: An integer representing the winning friend's number.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 5, k = 2
```

**Output:**
```text
3
```

**Explanation:**
Friends leave in order: 2, 4, 1, 5. The winner is 3.

### Example 2

**Input:**
```text
n = 6, k = 5
```

**Output:**
```text
1
```

**Explanation:**
Friends leave in order: 5, 4, 6, 2, 3. The winner is 1.

### Example 3

**Input:**
```text
n = 1, k = 1
```

**Output:**
```text
1
```

**Explanation:**
Only one player starts, winner is 1.

---

## Constraints

- `1 <= k <= n <= 500`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) with math/recursion or O(N) with queue`
