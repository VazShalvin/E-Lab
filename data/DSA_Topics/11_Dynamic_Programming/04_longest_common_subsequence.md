# 4. Longest Common Subsequence (LCS)

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: String, Dynamic Programming

---

## Problem Statement

Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

---

## Input & Output Format

- **Input**: Two strings `text1` and `text2`.
- **Output**: An integer representing the length of LCS.

---

## Sample Test Cases

### Example 1

**Input:**
```text
text1 = "abcde", text2 = "ace"
```

**Output:**
```text
3
```

**Explanation:**
The longest common subsequence is "ace" and its length is 3.

### Example 2

**Input:**
```text
text1 = "abc", text2 = "abc"
```

**Output:**
```text
3
```

**Explanation:**
The longest common subsequence is "abc".

### Example 3

**Input:**
```text
text1 = "abc", text2 = "def"
```

**Output:**
```text
0
```

**Explanation:**
There is no such common subsequence, so the result is 0.

---

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M * N) or O(min(M, N))`
