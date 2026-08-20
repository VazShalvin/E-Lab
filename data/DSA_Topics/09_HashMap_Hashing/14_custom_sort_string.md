# 14. Custom Sort String

**Topic**: HashMap / Hashing  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Sorting

---

## Problem Statement

You are given two strings `order` and `s`. All the characters of `order` are **unique** and were sorted in some custom order previously.

Permute the characters of `s` so that they match the order that `order` was sorted. More specifically, if a character `x` occurs before a character `y` in `order`, then `x` should occur before `y` in the permuted string.

Return any permutation of `s` that satisfies this property.

---

## Input & Output Format

- **Input**: Two strings `order` and `s`.
- **Output**: A string rearranged in the custom order.

---

## Sample Test Cases

### Example 1

**Input:**
```text
order = "cba", s = "abcd"
```

**Output:**
```text
"cbad"
```

**Explanation:**
"c", "b", and "a" appear in order. "d" not in order can be placed anywhere at the end.

### Example 2

**Input:**
```text
order = "cbafg", s = "abcd"
```

**Output:**
```text
"cbad"
```

**Explanation:**
'c', 'b', 'a' sorted first, followed by 'd'.

### Example 3

**Input:**
```text
order = "kqep", s = "pekeq"
```

**Output:**
```text
"kqeep"
```

**Explanation:**
Reordered matching order sequence.

---

## Constraints

- `1 <= order.length <= 26`
- `1 <= s.length <= 200`
- `order` and `s` consist of lowercase English letters.
- All the characters of `order` are **unique**.

---

## Complexity Analysis

- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(1)`
