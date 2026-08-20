# 15. Stamping the Sequence

**Topic**: Queue  
**Difficulty**: Hard  
**Tags**: String, Stack, Greedy, Queue

---

## Problem Statement

You are given two strings `stamp` and `target`. Initially, there is a string `s` of length `target.length` with all characters `s[i] == '?'`.

In each turn, you can place a stamp over `s` at index `i` (where `0 <= i <= target.length - stamp.length`) and replace the substring of `s` with `stamp`.

Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain `target` from `s` within `10 * target.length` turns, return an empty array.

---

## Input & Output Format

- **Input**: Two strings `stamp` and `target`.
- **Output**: An array of integers representing stamping indices.

---

## Sample Test Cases

### Example 1

**Input:**
```text
stamp = "abc", target = "ababc"
```

**Output:**
```text
[0, 2]
```

**Explanation:**
Initially s = "?????".
- Place stamp at 0: "abc??"
- Place stamp at 2: "ababc".

### Example 2

**Input:**
```text
stamp = "abca", target = "aabcaca"
```

**Output:**
```text
[3, 0, 1]
```

**Explanation:**
Can stamp in reverse using queue/matching.

### Example 3

**Input:**
```text
stamp = "a", target = "aaa"
```

**Output:**
```text
[0, 1, 2]
```

**Explanation:**
Stamp 1 char at a time across indices.

---

## Constraints

- `1 <= stamp.length <= target.length <= 1000`
- `stamp` and `target` consist of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N * (N - M))`
- **Space Complexity**: `O(N * (N - M))`
