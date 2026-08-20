# 5. Course Schedule II (Find Ordering)

**Topic**: Graph / BFS & DFS  
**Difficulty**: Medium  
**Tags**: Depth-First Search, Breadth-First Search, Graph, Topological Sort

---

## Problem Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return an **empty array**.

---

## Input & Output Format

- **Input**: An integer `numCourses` and a 2D array `prerequisites`.
- **Output**: An array of integers representing the course order.

---

## Sample Test Cases

### Example 1

**Input:**
```text
numCourses = 2, prerequisites = [[1, 0]]
```

**Output:**
```text
[0, 1]
```

**Explanation:**
Take course 0 first, then course 1.

### Example 2

**Input:**
```text
numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
```

**Output:**
```text
[0, 2, 1, 3]
```

**Explanation:**
[0, 1, 2, 3] is also a valid topological ordering.

### Example 3

**Input:**
```text
numCourses = 1, prerequisites = []
```

**Output:**
```text
[0]
```

**Explanation:**
Single course with no prerequisites.

---

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < numCourses`
- `a_i != b_i`

---

## Complexity Analysis

- **Time Complexity**: `O(V + E)`
- **Space Complexity**: `O(V + E)`
