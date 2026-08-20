# 1. Implement Trie (Prefix Tree)

**Topic**: Trie  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Design, Trie

---

## Problem Statement

A **trie** (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the `Trie` class:
- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

---

## Input & Output Format

- **Input**: Method calls and parameters.
- **Output**: Outputs corresponding to method calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

**Output:**
```text
[null, null, true, false, true, null, true]
```

**Explanation:**
Standard prefix tree operations.

### Example 2

**Input:**
```text
trie.search("banana");
```

**Output:**
```text
false
```

**Explanation:**
Word not inserted returns false.

### Example 3

**Input:**
```text
trie.startsWith("a");
```

**Output:**
```text
true
```

**Explanation:**
Prefix 'a' matches "apple" and "app".

---

## Constraints

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters.
- At most `3 * 10^4` calls in total will be made to `insert`, `search`, and `startsWith`.

---

## Complexity Analysis

- **Time Complexity**: `O(L) for insert, search, startsWith where L is word length`
- **Space Complexity**: `O(Total Characters)`
