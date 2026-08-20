# 15. Palindrome Pairs (Trie Matching)

**Topic**: Trie  
**Difficulty**: Hard  
**Tags**: Array, Hash Table, String, Trie

---

## Problem Statement

Given a list of **unique** words, return all the pairs of the **distinct** indices `(i, j)` in the given list, so that the concatenation of the two words `words[i] + words[j]` is a palindrome.

---

## Input & Output Format

- **Input**: An array of strings `words`.
- **Output**: A 2D array of index pairs `[[i, j], ...]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
words = ["abcd", "dcba", "lls", "s", "sssll"]
```

**Output:**
```text
[[0, 1], [1, 0], [3, 2], [2, 4]]
```

**Explanation:**
The palindromes are ["abcddcba", "dcbaabcd", "slls", "llssssll"].

### Example 2

**Input:**
```text
words = ["bat", "tab", "cat"]
```

**Output:**
```text
[[0, 1], [1, 0]]
```

**Explanation:**
The palindromes are ["battab", "tabbat"].

### Example 3

**Input:**
```text
words = ["a", ""]
```

**Output:**
```text
[[0, 1], [1, 0]]
```

**Explanation:**
["a", "a"].

---

## Constraints

- `1 <= words.length <= 5000`
- `0 <= words[i].length <= 300`
- `words[i]` consists of lower-case English letters.
- All words in `words` are unique.

---

## Complexity Analysis

- **Time Complexity**: `O(N * L^2)`
- **Space Complexity**: `O(N * L^2)`
