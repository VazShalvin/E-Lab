# 8. Decode Ways

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: String, Dynamic Programming

---

## Problem Statement

A message containing letters from `A-Z` can be encoded into numbers using the following mapping:
`'A' -> "1"`, `'B' -> "2"`, ..., `'Z' -> "26"`.

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above. Given a string `s` containing only digits, return the **number of ways** to decode it.

---

## Input & Output Format

- **Input**: A string `s` of digits.
- **Output**: An integer representing the total number of decoding combinations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "12"
```

**Output:**
```text
2
```

**Explanation:**
"12" could be decoded as "AB" (1 2) or "L" (12).

### Example 2

**Input:**
```text
s = "226"
```

**Output:**
```text
3
```

**Explanation:**
"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

### Example 3

**Input:**
```text
s = "06"
```

**Output:**
```text
0
```

**Explanation:**
"06" cannot be mapped to "F" because "6" is different from "06". Leading zero makes it invalid.

---

## Constraints

- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zero(s).

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
