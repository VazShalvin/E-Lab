# 10. Maximum Product of Word Lengths (Bitmasking)

**Topic**: Bit Manipulation  
**Difficulty**: Medium  
**Tags**: Array, String, Bit Manipulation

---

## Problem Statement

Given a string array `words`, return the maximum value of `length(word[i]) * length(word[j])` where the two words do not share common letters. If no such two words exist, return `0`.

---

## Input & Output Format

- **Input**: An array of strings `words`.
- **Output**: An integer representing the maximum length product.

---

## Sample Test Cases

### Example 1

**Input:**
```text
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
```

**Output:**
```text
16
```

**Explanation:**
The two words can be "abcw", "xtfn". Product of lengths = 4 * 4 = 16.

### Example 2

**Input:**
```text
words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
```

**Output:**
```text
4
```

**Explanation:**
The two words can be "ab", "cd". Lengths: 2 * 2 = 4.

### Example 3

**Input:**
```text
words = ["a", "aa", "aaa", "aaaa"]
```

**Output:**
```text
0
```

**Explanation:**
No such pair of words exist.

---

## Constraints

- `2 <= words.length <= 1000`
- `1 <= words[i].length <= 1000`
- `words[i]` consists only of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N^2 + L) where L is total characters`
- **Space Complexity**: `O(N)`
