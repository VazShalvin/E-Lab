# 14. Word Break (Trie-Optimized Dynamic Programming)

**Topic**: Trie  
**Difficulty**: Medium  
**Tags**: Array, String, Dynamic Programming, Trie

---

## Problem Statement

Given a string `s` and a dictionary of strings `wordDict`, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words using a **Trie** to optimize prefix lookup inside dynamic programming.

---

## Input & Output Format

- **Input**: A string `s` and a list of strings `wordDict`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "leetcode", wordDict = ["leet", "code"]
```

**Output:**
```text
true
```

**Explanation:**
"leetcode" -> "leet" (in Trie) + "code" (in Trie).

### Example 2

**Input:**
```text
s = "applepenapple", wordDict = ["apple", "pen"]
```

**Output:**
```text
true
```

**Explanation:**
"apple" + "pen" + "apple".

### Example 3

**Input:**
```text
s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
```

**Output:**
```text
false
```

**Explanation:**
Cannot segment completely.

---

## Constraints

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N * max_word_len)`
- **Space Complexity**: `O(N + Total Dictionary Characters)`
