# 5. Longest Word in Dictionary

**Topic**: Trie  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, String, Trie, Sorting

---

## Problem Statement

Given an array of strings `words` representing an English Dictionary, return the longest word in `words` that can be built one character at a time by other words in `words`.

If there is more than one possible answer, return the longest word with the **smallest lexicographical order**. If there is no answer, return the empty string `""`.

---

## Input & Output Format

- **Input**: An array of strings `words`.
- **Output**: A string representing the longest constructible word.

---

## Sample Test Cases

### Example 1

**Input:**
```text
words = ["w", "wo", "wor", "worl", "world"]
```

**Output:**
```text
"world"
```

**Explanation:**
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

### Example 2

**Input:**
```text
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
```

**Output:**
```text
"apple"
```

**Explanation:**
Both "apple" and "apply" can be built, but "apple" is lexicographically smaller than "apply".

### Example 3

**Input:**
```text
words = ["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte"]
```

**Output:**
```text
"latte"
```

**Explanation:**
"latte" is lexicographically smaller than "mocha".

---

## Constraints

- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 30`
- `words[i]` consists of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N * L)`
- **Space Complexity**: `O(N * L)`
