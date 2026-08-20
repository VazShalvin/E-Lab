# 6. First Unique Character in a Stream

**Topic**: Queue  
**Difficulty**: Medium  
**Tags**: Queue, Hash Table, String

---

## Problem Statement

Given a stream of characters, find the first non-repeating character each time a character is inserted into the stream. If there is no unique character at any point, output `#`.

---

## Input & Output Format

- **Input**: A string `A` representing the character stream.
- **Output**: A string where the `i-th` character is the first non-repeating character after processing the `i-th` character.

---

## Sample Test Cases

### Example 1

**Input:**
```text
A = "aabc"
```

**Output:**
```text
"a#bb"
```

**Explanation:**
After 'a' -> 'a'
After 'a' -> '#' (no unique)
After 'b' -> 'b'
After 'c' -> 'b'

### Example 2

**Input:**
```text
A = "zz"
```

**Output:**
```text
"z#"
```

**Explanation:**
After 'z' -> 'z', after second 'z' -> '#'

### Example 3

**Input:**
```text
A = "abcab"
```

**Output:**
```text
"aaabc"
```

**Explanation:**
Maintains FIFO unique tracking.

---

## Constraints

- `1 <= A.length <= 10^5`
- `A` consists of lowercase English characters.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) (bounded by alphabet size)`
