# 8. Longest Palindromic Substring

**Topic**: String  
**Difficulty**: Medium  
**Tags**: Two Pointers, String, Dynamic Programming

---

## Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: A string representing the longest palindromic substring.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "babad"
```

**Output:**
```text
"bab"
```

**Explanation:**
"aba" is also a valid answer.

### Example 2

**Input:**
```text
s = "cbbd"
```

**Output:**
```text
"bb"
```

**Explanation:**
The longest palindromic substring is "bb".

### Example 3

**Input:**
```text
s = "a"
```

**Output:**
```text
"a"
```

**Explanation:**
A single character is always a palindrome.

---

## Constraints

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(1)`
