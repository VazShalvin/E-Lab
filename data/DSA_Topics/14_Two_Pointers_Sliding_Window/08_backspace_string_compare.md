# 8. Backspace String Compare (O(1) Space)

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Easy  
**Tags**: Two Pointers, String, Stack, Simulation

---

## Problem Statement

Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Can you solve it in `O(n)` time and `O(1)` space using two pointers traversing backwards?

---

## Input & Output Format

- **Input**: Two strings `s` and `t`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "ab#c", t = "ad#c"
```

**Output:**
```text
true
```

**Explanation:**
Both s and t become "ac".

### Example 2

**Input:**
```text
s = "ab##", t = "c#d#"
```

**Output:**
```text
true
```

**Explanation:**
Both s and t become "".

### Example 3

**Input:**
```text
s = "a#c", t = "b"
```

**Output:**
```text
false
```

**Explanation:**
s becomes "c" while t becomes "b".

---

## Constraints

- `1 <= s.length, t.length <= 200`
- `s` and `t` only contain lowercase letters and `'#'` characters.

---

## Complexity Analysis

- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(1)`
