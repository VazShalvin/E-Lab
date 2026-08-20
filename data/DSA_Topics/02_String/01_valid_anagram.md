# 1. Valid Anagram

**Topic**: String  
**Difficulty**: Easy  
**Tags**: Hash Table, String, Sorting

---

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## Input & Output Format

- **Input**: Two strings `s` and `t`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "anagram", t = "nagaram"
```

**Output:**
```text
true
```

**Explanation:**
Both strings contain the exact same count of each character.

### Example 2

**Input:**
```text
s = "rat", t = "car"
```

**Output:**
```text
false
```

**Explanation:**
'rat' and 'car' have different characters.

### Example 3

**Input:**
```text
s = "a", t = "ab"
```

**Output:**
```text
false
```

**Explanation:**
Lengths differ, so they cannot be anagrams.

---

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
