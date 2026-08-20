# 10. Longest Substring with At Most K Distinct Characters

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Sliding Window

---

## Problem Statement

Given a string `s` and an integer `k`, return the length of the longest substring of `s` that contains at most `k` distinct characters.

---

## Input & Output Format

- **Input**: A string `s` and an integer `k`.
- **Output**: An integer representing the maximum length.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "eceba", k = 2
```

**Output:**
```text
3
```

**Explanation:**
The substring is "ece" with length 3.

### Example 2

**Input:**
```text
s = "aa", k = 1
```

**Output:**
```text
2
```

**Explanation:**
The substring is "aa" with length 2.

### Example 3

**Input:**
```text
s = "a", k = 0
```

**Output:**
```text
0
```

**Explanation:**
k = 0 returns 0.

---

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `0 <= k <= 50`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(k)`
