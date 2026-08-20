# 14. H-Index

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, Sorting, Counting Sort

---

## Problem Statement

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i-th` paper, return the researcher's **h-index**.

According to the definition of h-index on Wikipedia: A scientist has an index `h` if `h` of their `n` papers have at least `h` citations each, and the other `n − h` papers have no more than `h` citations each.

---

## Input & Output Format

- **Input**: An array of integers `citations`.
- **Output**: An integer representing the h-index.

---

## Sample Test Cases

### Example 1

**Input:**
```text
citations = [3, 0, 6, 1, 5]
```

**Output:**
```text
3
```

**Explanation:**
[3, 0, 6, 1, 5] means the researcher has 5 papers with 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

### Example 2

**Input:**
```text
citations = [1, 3, 1]
```

**Output:**
```text
1
```

**Explanation:**
h-index is 1.

### Example 3

**Input:**
```text
citations = [100]
```

**Output:**
```text
1
```

**Explanation:**
Single paper with 100 citations gives h-index 1.

---

## Constraints

- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N) Counting Sort or O(N log N)`
- **Space Complexity**: `O(N)`
