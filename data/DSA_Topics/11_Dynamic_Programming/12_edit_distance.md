# 12. Edit Distance (Levenshtein Distance)

**Topic**: Dynamic Programming  
**Difficulty**: Medium  
**Tags**: String, Dynamic Programming

---

## Problem Statement

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

---

## Input & Output Format

- **Input**: Two strings `word1` and `word2`.
- **Output**: An integer representing the minimum operations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
word1 = "horse", word2 = "ros"
```

**Output:**
```text
3
```

**Explanation:**
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

### Example 2

**Input:**
```text
word1 = "intention", word2 = "execution"
```

**Output:**
```text
5
```

**Explanation:**
intention -> inention -> enention -> exention -> exection -> execution

### Example 3

**Input:**
```text
word1 = "", word2 = "a"
```

**Output:**
```text
1
```

**Explanation:**
Insert 'a'.

---

## Constraints

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M * N)`
