# 14. Remove Duplicate Letters (Smallest Lexicographical String)

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: String, Stack, Greedy, Monotonic Stack

---

## Problem Statement

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: A string with unique characters in smallest lexicographical order.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "bcabc"
```

**Output:**
```text
"abc"
```

**Explanation:**
"abc" is smallest lexicographical order.

### Example 2

**Input:**
```text
s = "cbacdcbc"
```

**Output:**
```text
"acdb"
```

**Explanation:**
Removing duplicates preserves character order to give "acdb".

### Example 3

**Input:**
```text
s = "abacb"
```

**Output:**
```text
"abc"
```

**Explanation:**
"abc" is the smallest.

---

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
