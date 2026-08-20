# 13. Longest Common Prefix

**Topic**: String  
**Difficulty**: Easy  
**Tags**: String, Trie

---

## Problem Statement

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---

## Input & Output Format

- **Input**: An array of strings `strs`.
- **Output**: A string representing the longest common prefix.

---

## Sample Test Cases

### Example 1

**Input:**
```text
strs = ["flower", "flow", "flight"]
```

**Output:**
```text
"fl"
```

**Explanation:**
"fl" is common to all three words.

### Example 2

**Input:**
```text
strs = ["dog", "racecar", "car"]
```

**Output:**
```text
""
```

**Explanation:**
There is no common prefix among the input strings.

### Example 3

**Input:**
```text
strs = ["interspecies", "interstellar", "interstate"]
```

**Output:**
```text
"inters"
```

**Explanation:**
"inters" is common to all strings.

---

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(S) where S is sum of characters in all strings`
- **Space Complexity**: `O(1)`
