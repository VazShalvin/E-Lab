# 6. Combination Sum II (Each Candidate Used Once)

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: Array, Backtracking

---

## Problem Statement

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

Note: The solution set must not contain duplicate combinations.

---

## Input & Output Format

- **Input**: An array of integers `candidates` and an integer `target`.
- **Output**: A 2D array of unique combinations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
```

**Output:**
```text
[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
```

**Explanation:**
Four distinct combinations.

### Example 2

**Input:**
```text
candidates = [2, 5, 2, 1, 2], target = 5
```

**Output:**
```text
[[1, 2, 2], [5]]
```

**Explanation:**
Two unique combinations.

### Example 3

**Input:**
```text
candidates = [1, 1], target = 1
```

**Output:**
```text
[[1]]
```

**Explanation:**
Only one [1] is output.

---

## Constraints

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

---

## Complexity Analysis

- **Time Complexity**: `O(2^N)`
- **Space Complexity**: `O(N)`
