# 10. Encode and Decode Strings

**Topic**: String  
**Difficulty**: Medium  
**Tags**: Array, String, Design

---

## Problem Statement

Design an algorithm to encode a list of strings to a single string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement `encode` and `decode` methods.

---

## Input & Output Format

- **Input**: A list of strings `strs`.
- **Output**: The identical reconstructed list of strings.

---

## Sample Test Cases

### Example 1

**Input:**
```text
strs = ["lint", "code", "love", "you"]
```

**Output:**
```text
["lint", "code", "love", "you"]
```

**Explanation:**
Can encode with length-prefix like '4#lint4#code4#love3#you' and accurately decode back.

### Example 2

**Input:**
```text
strs = ["we", "say", ":", "yes"]
```

**Output:**
```text
["we", "say", ":", "yes"]
```

**Explanation:**
Handles special characters and delimiters cleanly.

### Example 3

**Input:**
```text
strs = [""]
```

**Output:**
```text
[""]
```

**Explanation:**
Correctly encodes and decodes an empty string as a list element.

---

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` contains any possible characters out of 256 valid ASCII characters.

---

## Complexity Analysis

- **Time Complexity**: `O(N) for both encode and decode`
- **Space Complexity**: `O(N)`
