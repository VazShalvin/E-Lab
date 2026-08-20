# 5. Word Break

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, String, Dynamic Programming, Trie, Memoization

---

## Problem Statement

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

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
Return true because "leetcode" can be segmented as "leet code".

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
Return true because "applepenapple" can be segmented as "apple pen apple".

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
Cannot segment completely into valid dictionary words.

---

## Constraints

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

---

## Complexity Analysis

- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N)`
