# 4. Longest Repeating Character Replacement

**Topic**: String  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Sliding Window

---

## Problem Statement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

---

## Input & Output Format

- **Input**: A string `s` and an integer `k`.
- **Output**: An integer representing the maximum length.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "ABAB", k = 2
```

**Output:**
```text
4
```

**Explanation:**
Replace the two 'A's with two 'B's or vice versa to get "BBBB" or "AAAA".

### Example 2

**Input:**
```text
s = "AABABBA", k = 1
```

**Output:**
```text
4
```

**Explanation:**
Replace the middle 'A' with 'B' to form "AABBBBA". The substring "BBBB" has the longest repeating letters, which is 4.

### Example 3

**Input:**
```text
s = "AAAA", k = 2
```

**Output:**
```text
4
```

**Explanation:**
All characters are already identical.

---

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
