# 6. Queue Reconstruction by Height

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: Array, Greedy, Binary Indexed Tree, Segment Tree, Sorting

---

## Problem Statement

You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each `people[i] = [h_i, k_i]` represents the `i-th` person of height `h_i` with **exactly** `k_i` other people in front who have a height greater than or equal to `h_i`.

Reconstruct and return the queue that is represented by the input array `people`.

---

## Input & Output Format

- **Input**: A 2D array `people`.
- **Output**: A 2D array representing reconstructed queue.

---

## Sample Test Cases

### Example 1

**Input:**
```text
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
```

**Output:**
```text
[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
```

**Explanation:**
Reconstructed matching height and count conditions.

### Example 2

**Input:**
```text
people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
```

**Output:**
```text
[[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]
```

**Explanation:**
Valid reconstructed queue.

### Example 3

**Input:**
```text
people = [[1, 0]]
```

**Output:**
```text
[[1, 0]]
```

**Explanation:**
Single person queue.

---

## Constraints

- `1 <= people.length <= 2000`
- `0 <= h_i <= 10^6`
- `0 <= k_i < people.length`
- It is guaranteed that the queue can be reconstructed.

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`
