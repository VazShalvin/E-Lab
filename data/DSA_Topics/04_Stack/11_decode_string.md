# 11. Decode String

**Topic**: Stack  
**Difficulty**: Medium  
**Tags**: String, Stack, Recursion

---

## Problem Statement

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

---

## Input & Output Format

- **Input**: An encoded string `s`.
- **Output**: Decoded string.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "3[a]2[bc]"
```

**Output:**
```text
"aaabcbc"
```

**Explanation:**
"a" repeated 3 times + "bc" repeated 2 times.

### Example 2

**Input:**
```text
s = "3[a2[c]]"
```

**Output:**
```text
"accaccacc"
```

**Explanation:**
Inner "2[c]" -> "cc", then "a" + "cc" -> "acc" repeated 3 times.

### Example 3

**Input:**
```text
s = "2[abc]3[cd]ef"
```

**Output:**
```text
"abcabccdcdcdef"
```

**Explanation:**
"abc"*2 + "cd"*3 + "ef".

---

## Constraints

- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
- `s` is guaranteed to be a valid input.

---

## Complexity Analysis

- **Time Complexity**: `O(maxK * N)`
- **Space Complexity**: `O(N)`
