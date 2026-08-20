# 9. Task Scheduler

**Topic**: Queue  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Greedy, Queue, Heap

---

## Problem Statement

You are given an array of CPU `tasks`, each represented by letters A to Z, and a cooling interval `n`. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: **identical** tasks must be separated by at least `n` intervals with other tasks or idle time.

Return the minimum number of CPU cycles required to complete all tasks.

---

## Input & Output Format

- **Input**: An array of characters `tasks` and an integer `n`.
- **Output**: An integer representing the minimum CPU units of time.

---

## Sample Test Cases

### Example 1

**Input:**
```text
tasks = ["A", "A", "A", "B", "B", "B"], n = 2
```

**Output:**
```text
8
```

**Explanation:**
A -> B -> idle -> A -> B -> idle -> A -> B.
Total time: 8.

### Example 2

**Input:**
```text
tasks = ["A", "C", "A", "B", "D", "B"], n = 1
```

**Output:**
```text
6
```

**Explanation:**
A -> B -> C -> A -> D -> B. No idle time needed.

### Example 3

**Input:**
```text
tasks = ["A", "A", "A", "B", "B", "B"], n = 0
```

**Output:**
```text
6
```

**Explanation:**
Cooling period is 0, execution takes 6 units.

---

## Constraints

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is upper-case English letter.
- The integer `n` is in the range `[0, 100]`.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
