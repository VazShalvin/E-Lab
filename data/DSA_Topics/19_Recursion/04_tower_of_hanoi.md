# 4. Tower of Hanoi

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: Recursion

---

## Problem Statement

The tower of Hanoi is a famous puzzle where we have three rods (`from_rod`, `to_rod`, `aux_rod`) and `N` disks. The objective is to move the entire stack to another rod obeying the following rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one stack and placing it on top of another stack.
3. No disk may be placed on top of a smaller disk.

Print all disk moves and return the total number of moves.

---

## Input & Output Format

- **Input**: An integer `N` representing the number of disks.
- **Output**: An integer representing the total moves `2^N - 1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
N = 2
```

**Output:**
```text
3 moves
move disk 1 from rod 1 to rod 2
move disk 2 from rod 1 to rod 3
move disk 1 from rod 2 to rod 3
```

**Explanation:**
Total 2^2 - 1 = 3 moves.

### Example 2

**Input:**
```text
N = 3
```

**Output:**
```text
7 moves
```

**Explanation:**
2^3 - 1 = 7 moves.

### Example 3

**Input:**
```text
N = 1
```

**Output:**
```text
1 move
move disk 1 from rod 1 to rod 3
```

**Explanation:**
Single move directly to target.

---

## Constraints

- `1 <= N <= 16`

---

## Complexity Analysis

- **Time Complexity**: `O(2^N)`
- **Space Complexity**: `O(N) recursion stack`
