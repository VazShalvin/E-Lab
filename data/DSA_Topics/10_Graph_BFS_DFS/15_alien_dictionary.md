# 15. Alien Dictionary (Topological Sort on Lexicographical Order)

**Topic**: Graph / BFS & DFS  
**Difficulty**: Hard  
**Tags**: Array, String, Graph, Topological Sort

---

## Problem Statement

There is a new alien language that uses the English alphabet. However, the order among letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are **sorted lexicographically** by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in **lexicographically increasing order** by the new language's rules. If there is no solution, return `""`. If there are multiple solutions, return **any of them**.

---

## Input & Output Format

- **Input**: An array of strings `words`.
- **Output**: A string representing the alien alphabetical order, or `""`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
words = ["wrt", "wrf", "er", "ett", "rftt"]
```

**Output:**
```text
"wertf"
```

**Explanation:**
Comparing adjacent words gives ordering:
't' < 'f'
'w' < 'e'
'r' < 't'
'e' < 'r'
Topological sort gives "wertf".

### Example 2

**Input:**
```text
words = ["z", "x"]
```

**Output:**
```text
"zx"
```

**Explanation:**
'z' comes before 'x'.

### Example 3

**Input:**
```text
words = ["z", "x", "z"]
```

**Output:**
```text
""
```

**Explanation:**
'z' < 'x' and 'x' < 'z' contains a cycle, impossible order.

---

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(C) where C is total length of all words`
- **Space Complexity**: `O(1) (bounded by alphabet size)`
