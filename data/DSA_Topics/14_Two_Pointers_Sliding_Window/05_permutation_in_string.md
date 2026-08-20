# 5. Permutation in String (Sliding Window Anagram Match)

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Hash Table, Two Pointers, String, Sliding Window

---

## Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the **substring** of `s2`.

---

## Input & Output Format

- **Input**: Two strings `s1` and `s2`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
s1 = "ab", s2 = "eidbaooo"
```

**Output:**
```text
true
```

**Explanation:**
s2 contains one permutation of s1 ("ba").

### Example 2

**Input:**
```text
s1 = "ab", s2 = "eidboaoo"
```

**Output:**
```text
false
```

**Explanation:**
No permutation of s1 exists as a contiguous substring.

### Example 3

**Input:**
```text
s1 = "adc", s2 = "dcda"
```

**Output:**
```text
true
```

**Explanation:**
"cda" contains "adc".

---

## Constraints

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) (frequency size 26)`
