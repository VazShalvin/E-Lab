# 8. Palindrome Partitioning

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: String, Dynamic Programming, Backtracking

---

## Problem Statement

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**.

Return all possible palindrome partitioning of `s`.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: A 2D array of strings representing partitions.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "aab"
```

**Output:**
```text
[["a", "a", "b"], ["aa", "b"]]
```

**Explanation:**
Two valid palindrome partitionings.

### Example 2

**Input:**
```text
s = "a"
```

**Output:**
```text
[["a"]]
```

**Explanation:**
Single partition.

### Example 3

**Input:**
```text
s = "racecar"
```

**Output:**
```text
[["r", "a", "c", "e", "c", "a", "r"], ["r", "a", "cec", "a", "r"], ["r", "aceca", "r"], ["racecar"]]
```

**Explanation:**
All valid partitions where every part is a palindrome.

---

## Constraints

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(N)`
