# 6. Reorganize String

**Topic**: Heap / Priority Queue  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Greedy, Sorting, Heap, Counting

---

## Problem Statement

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

Return any possible rearrangement of `s` or return `""` if not possible.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: A valid rearranged string, or `""`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "aab"
```

**Output:**
```text
"aba"
```

**Explanation:**
No two adjacent characters are identical.

### Example 2

**Input:**
```text
s = "aaab"
```

**Output:**
```text
""
```

**Explanation:**
'a' appears 3 times in length 4 string, impossible to separate.

### Example 3

**Input:**
```text
s = "vvvlo"
```

**Output:**
```text
"vlvov"
```

**Explanation:**
Valid rearrangement.

---

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N log A) where A is alphabet size`
- **Space Complexity**: `O(A)`
