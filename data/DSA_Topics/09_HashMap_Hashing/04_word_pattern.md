# 4. Word Pattern

**Topic**: HashMap / Hashing  
**Difficulty**: Easy  
**Tags**: Hash Table, String

---

## Problem Statement

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`.

---

## Input & Output Format

- **Input**: A string `pattern` and a string `s`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
pattern = "abba", s = "dog cat cat dog"
```

**Output:**
```text
true
```

**Explanation:**
'a' -> "dog", 'b' -> "cat".

### Example 2

**Input:**
```text
pattern = "abba", s = "dog cat cat fish"
```

**Output:**
```text
false
```

**Explanation:**
'a' maps to both "dog" and "fish".

### Example 3

**Input:**
```text
pattern = "aaaa", s = "dog cat cat dog"
```

**Output:**
```text
false
```

**Explanation:**
'a' maps to multiple different words.

---

## Constraints

- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters.
- `1 <= s.length <= 3000`
- `s` contains only lowercase English letters and spaces `' '`.

---

## Complexity Analysis

- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
