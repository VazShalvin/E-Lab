# 11. Prefix and Suffix Search

**Topic**: Trie  
**Difficulty**: Hard  
**Tags**: Array, Hash Table, String, Design, Trie

---

## Problem Statement

Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the `WordFilter` class:
- `WordFilter(string[] words)` Initializes the object with the `words` in the dictionary.
- `f(string pref, string suff)` Returns the index of the word in the dictionary, which has the prefix `pref` and the suffix `suff`. If there is more than one valid index, return **the largest** of them. If there is no such word in the dictionary, return `-1`.

---

## Input & Output Format

- **Input**: Constructor word array and query strings `pref` and `suff`.
- **Output**: Integer largest index or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
```

**Output:**
```text
[null, 0]
```

**Explanation:**
Inserted with wrapped suffix delimiters: "e{apple", "le{apple", etc.

### Example 2

**Input:**
```text
wordFilter.f("b", "e");
```

**Output:**
```text
-1
```

**Explanation:**
No matching word found.

### Example 3

**Input:**
```text
WordFilter wf = new WordFilter(["apple", "ape"]); wf.f("ap", "e");
```

**Output:**
```text
1
```

**Explanation:**
Both match, largest index 1 returned.

---

## Constraints

- `1 <= words.length <= 10^4`
- `1 <= words[i].length <= 7`
- `1 <= pref.length, suff.length <= 7`
- `words[i]`, `pref` and `suff` consist of lowercase English letters only.
- At most `10^4` calls will be made to the function `f`.

---

## Complexity Analysis

- **Time Complexity**: `O(N * L^2) init, O(pref + suff) per query`
- **Space Complexity**: `O(N * L^2)`
