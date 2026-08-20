# 4. Partition Labels

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: Hash Table, Two Pointers, String, Greedy

---

## Problem Statement

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return a list of integers representing the size of these parts.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: A list of integers representing partition sizes.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "ababcbacadefegdehijhklij"
```

**Output:**
```text
[9, 7, 8]
```

**Explanation:**
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

### Example 2

**Input:**
```text
s = "eccbbbbdec"
```

**Output:**
```text
[10]
```

**Explanation:**
The entire string is the only valid partition.

### Example 3

**Input:**
```text
s = "abc"
```

**Output:**
```text
[1, 1, 1]
```

**Explanation:**
Each character appears once.

---

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1) (26 letters)`
