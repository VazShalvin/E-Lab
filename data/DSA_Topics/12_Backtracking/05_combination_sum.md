# 5. Combination Sum

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: Array, Backtracking

---

## Problem Statement

Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**.

---

## Input & Output Format

- **Input**: An array of integers `candidates` and an integer `target`.
- **Output**: A 2D array of combinations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
candidates = [2, 3, 6, 7], target = 7
```

**Output:**
```text
[[2, 2, 3], [7]]
```

**Explanation:**
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times. 7 is a candidate, and 7 = 7.

### Example 2

**Input:**
```text
candidates = [2, 3, 5], target = 8
```

**Output:**
```text
[[2, 2, 2, 2], [2, 3, 3], [3, 5]]
```

**Explanation:**
Three valid combinations.

### Example 3

**Input:**
```text
candidates = [2], target = 1
```

**Output:**
```text
[]
```

**Explanation:**
No combination sums to 1.

---

## Constraints

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 40`

---

## Complexity Analysis

- **Time Complexity**: `O(2^(target / min_val))`
- **Space Complexity**: `O(target / min_val)`
