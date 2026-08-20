# 8. Word Ladder (Shortest Transformation)

**Topic**: Graph / BFS & DFS  
**Difficulty**: Hard  
**Tags**: Hash Table, String, Breadth-First Search

---

## Problem Statement

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s_1 -> s_2 -> ... -> s_k` such that:
- Every adjacent pair of words differs by a single letter.
- Every `s_i` for `1 <= i <= k` is in `wordList`.
- `s_k == endWord`.

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the **number of words** in the **shortest transformation sequence** from `beginWord` to `endWord`, or `0` if no such sequence exists.

---

## Input & Output Format

- **Input**: Two strings `beginWord` and `endWord`, and an array of strings `wordList`.
- **Output**: An integer representing the sequence length.

---

## Sample Test Cases

### Example 1

**Input:**
```text
beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
```

**Output:**
```text
5
```

**Explanation:**
One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.

### Example 2

**Input:**
```text
beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log"]
```

**Output:**
```text
0
```

**Explanation:**
The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

### Example 3

**Input:**
```text
beginWord = "a", endWord = "c", wordList = ["a", "b", "c"]
```

**Output:**
```text
2
```

**Explanation:**
"a" -> "c" (length 2).

---

## Constraints

- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- All strings in `wordList` are **unique**.

---

## Complexity Analysis

- **Time Complexity**: `O(M^2 * N) where M is word length, N is word list size`
- **Space Complexity**: `O(M * N)`
