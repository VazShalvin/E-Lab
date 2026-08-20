# 10. Asteroid Collision

**Topic**: Stack  
**Difficulty**: Medium  
**Tags**: Array, Stack, Simulation

---

## Problem Statement

We are given an array `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

---

## Input & Output Format

- **Input**: An array of integers `asteroids`.
- **Output**: An array of remaining asteroid integers.

---

## Sample Test Cases

### Example 1

**Input:**
```text
asteroids = [5, 10, -5]
```

**Output:**
```text
[5, 10]
```

**Explanation:**
10 and -5 collide resulting in 10. 5 and 10 never collide.

### Example 2

**Input:**
```text
asteroids = [8, -8]
```

**Output:**
```text
[]
```

**Explanation:**
8 and -8 collide and both explode.

### Example 3

**Input:**
```text
asteroids = [10, 2, -5]
```

**Output:**
```text
[10]
```

**Explanation:**
2 and -5 collide resulting in -5. 10 and -5 collide resulting in 10.

---

## Constraints

- `2 <= asteroids.length <= 10^4`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
