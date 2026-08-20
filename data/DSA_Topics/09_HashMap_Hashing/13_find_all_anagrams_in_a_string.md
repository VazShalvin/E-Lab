# 13. Find All Anagrams in a String

**Topic**: HashMap / Hashing  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Sliding Window

---

## Problem Statement

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in **any order**.

---

## Input & Output Format

- **Input**: Two strings `s` and `p`.
- **Output**: An array of integers representing start indices.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "cbaebabacd", p = "abc"
```

**Output:**
```text
[0, 6]
```

**Explanation:**
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

### Example 2

**Input:**
```text
s = "abab", p = "ab"
```

**Output:**
```text
[0, 1, 2]
```

**Explanation:**
Substrings at indices 0, 1, 2 are "ab", "ba", "ab".

### Example 3

**Input:**
```text
s = "a", p = "a"
```

**Output:**
```text
[0]
```

**Explanation:**
Index 0 matches.

---

## Constraints

- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) (frequency table of 26)`
