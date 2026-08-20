# 10. Concatenated Words

**Topic**: Trie  
**Difficulty**: Hard  
**Tags**: Array, String, Dynamic Programming, Depth-First Search, Trie

---

## Problem Statement

Given an array of strings `words` (**without duplicates**), return all the **concatenated words** in the given list of `words`.

A **concatenated word** is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.

---

## Input & Output Format

- **Input**: An array of strings `words`.
- **Output**: A list of concatenated words.

---

## Sample Test Cases

### Example 1

**Input:**
```text
words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
```

**Output:**
```text
["catsdogcats", "dogcatsdog", "ratcatdogcat"]
```

**Explanation:**
"catsdogcats" = "cats" + "dog" + "cats"
"dogcatsdog" = "dog" + "cats" + "dog"
"ratcatdogcat" = "rat" + "cat" + "dog" + "cat".

### Example 2

**Input:**
```text
words = ["cat", "dog", "catdog"]
```

**Output:**
```text
["catdog"]
```

**Explanation:**
"catdog" = "cat" + "dog".

### Example 3

**Input:**
```text
words = ["a", "b", "ab", "abc"]
```

**Output:**
```text
["ab"]
```

**Explanation:**
"ab" = "a" + "b".

---

## Constraints

- `1 <= words.length <= 10^4`
- `1 <= words[i].length <= 30`
- `words[i]` consists of only lowercase English letters.
- All strings in `words` are **unique**.
- `1 <= sum(words[i].length) <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(N * L^2)`
- **Space Complexity**: `O(N * L)`
