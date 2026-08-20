# 6. Group Anagrams

**Topic**: String  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, String, Sorting

---

## Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## Input & Output Format

- **Input**: An array of strings `strs`.
- **Output**: A 2D array of grouped strings.

---

## Sample Test Cases

### Example 1

**Input:**
```text
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Output:**
```text
[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

**Explanation:**
The grouped anagrams share identical character counts.

### Example 2

**Input:**
```text
strs = [""]
```

**Output:**
```text
[[""]]
```

**Explanation:**
Single empty string forms its own group.

### Example 3

**Input:**
```text
strs = ["a"]
```

**Output:**
```text
[["a"]]
```

**Explanation:**
Single character string forms its own group.

---

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N * K log K) or O(N * K)`
- **Space Complexity**: `O(N * K)`
