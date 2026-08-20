# 3. Isomorphic Strings

**Topic**: HashMap / Hashing  
**Difficulty**: Easy  
**Tags**: Hash Table, String

---

## Problem Statement

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

---

## Input & Output Format

- **Input**: Two strings `s` and `t`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "egg", t = "add"
```

**Output:**
```text
true
```

**Explanation:**
'e' -> 'a', 'g' -> 'd'.

### Example 2

**Input:**
```text
s = "foo", t = "bar"
```

**Output:**
```text
false
```

**Explanation:**
'o' cannot map to both 'a' and 'r'.

### Example 3

**Input:**
```text
s = "paper", t = "title"
```

**Output:**
```text
true
```

**Explanation:**
'p'->'t', 'a'->'i', 'e'->'l', 'r'->'e'.

---

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ASCII character.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) (ASCII bounded)`
