# 3. Longest Substring Without Repeating Characters

**Topic**: String  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Sliding Window

---

## Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: An integer representing the length of the longest substring.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "abcabcbb"
```

**Output:**
```text
3
```

**Explanation:**
The answer is "abc", with the length of 3.

### Example 2

**Input:**
```text
s = "bbbbb"
```

**Output:**
```text
1
```

**Explanation:**
The answer is "b", with the length of 1.

### Example 3

**Input:**
```text
s = "pwwkew"
```

**Output:**
```text
3
```

**Explanation:**
The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

---

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(min(N, M)) where M is character set size`
