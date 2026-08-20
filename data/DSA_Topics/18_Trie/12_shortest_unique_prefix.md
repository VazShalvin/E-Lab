# 12. Shortest Unique Prefix for Every Word

**Topic**: Trie  
**Difficulty**: Medium  
**Tags**: Array, String, Trie

---

## Problem Statement

Given an array of words, find the **shortest unique prefix** for each word in the array. You can assume that no word is prefix of another word.

---

## Input & Output Format

- **Input**: An array of strings `words`.
- **Output**: An array of shortest unique prefix strings.

---

## Sample Test Cases

### Example 1

**Input:**
```text
words = ["zebra", "dog", "duck", "dove"]
```

**Output:**
```text
["z", "dog", "du", "dov"]
```

**Explanation:**
"z" uniquely identifies "zebra". "du" uniquely identifies "duck". "dov" identifies "dove" vs "dog".

### Example 2

**Input:**
```text
words = ["geeksgeeks", "geeksquiz", "geeksforgeeks"]
```

**Output:**
```text
["geeksg", "geeksq", "geeksf"]
```

**Explanation:**
Unique prefix computed where branch frequency drops to 1.

### Example 3

**Input:**
```text
words = ["apple", "banana"]
```

**Output:**
```text
["a", "b"]
```

**Explanation:**
"a" and "b".

---

## Constraints

- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 50`
- All words consist of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N * L)`
- **Space Complexity**: `O(N * L)`
