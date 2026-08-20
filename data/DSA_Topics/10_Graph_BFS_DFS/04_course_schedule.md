# 4. Course Schedule (Cycle Detection / Topological Sort)

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Depth-First Search, Breadth-First Search, Graph, Topological Sort

---

## Problem Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

Return `true` if you can finish all courses. Otherwise, return `false`.

---

## Input & Output Format

- **Input**: An integer `numCourses` and a 2D array `prerequisites`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
numCourses = 2, prerequisites = [[1, 0]]
```

**Output:**
```text
true
```

**Explanation:**
There are 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

### Example 2

**Input:**
```text
numCourses = 2, prerequisites = [[1, 0], [0, 1]]
```

**Output:**
```text
false
```

**Explanation:**
There is a circular dependency (cycle) between course 0 and course 1.

### Example 3

**Input:**
```text
numCourses = 3, prerequisites = [[0, 1], [0, 2], [1, 2]]
```

**Output:**
```text
true
```

**Explanation:**
DAG with topological ordering [2, 1, 0].

---

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < numCourses`
- All prerequisite pairs are **unique**.

---

## Complexity Analysis

- **Time Complexity**: `O(V + E)`
- **Space Complexity**: `O(V + E)`
