# 9. Palindromic Substrings

**Topic**: String  
**Difficulty**: Medium  
**Tags**: Two Pointers, String, Dynamic Programming

---

## Problem Statement

Given a string `s`, return the number of **palindromic substrings** in it.

A string is a **palindrome** when it reads the same backward as forward.
A **substring** is a contiguous sequence of characters within the string.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: An integer representing the count of palindromic substrings.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "abc"
```

**Output:**
```text
3
```

**Explanation:**
Three palindromic substrings: "a", "b", "c".

### Example 2

**Input:**
```text
s = "aaa"
```

**Output:**
```text
6
```

**Explanation:**
Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".

### Example 3

**Input:**
```text
s = "racecar"
```

**Output:**
```text
10
```

**Explanation:**
Palindromic substrings include "r", "a", "c", "e", "c", "a", "r", "cec", "aceca", "racecar".

---

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(1)`
