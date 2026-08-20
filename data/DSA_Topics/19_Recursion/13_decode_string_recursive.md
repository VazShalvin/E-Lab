# 13. Decode String (Recursive Parser)

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: String, Stack, Recursion

---

## Problem Statement

Given an encoded string `s`, implement a clean **pure recursive parser** to return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times.

---

## Input & Output Format

- **Input**: An encoded string `s`.
- **Output**: The decoded string.

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
Recursive evaluation of nested brackets.

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
Unfolds sequentially.

---

## Constraints

- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.

---

## Complexity Analysis

- **Time Complexity**: `O(Output Length)`
- **Space Complexity**: `O(N) recursion stack`
