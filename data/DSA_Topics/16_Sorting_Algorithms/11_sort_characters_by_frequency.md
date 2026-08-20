# 11. Sort Characters By Frequency

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Sorting, Heap, Bucket Sort, Counting

---

## Problem Statement

Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The **frequency** of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: A string sorted by character frequency.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "tree"
```

**Output:**
```text
"eert"
```

**Explanation:**
'e' appears twice, while 'r' and 't' appear once. "eetr" is also a valid answer.

### Example 2

**Input:**
```text
s = "cccaaa"
```

**Output:**
```text
"aaaccc"
```

**Explanation:**
Both 'c' and 'a' appear three times, so "cccaaa" is also valid.

### Example 3

**Input:**
```text
s = "Aabb"
```

**Output:**
```text
"bbAa"
```

**Explanation:**
'b' appears twice, 'A' and 'a' appear once.

---

## Constraints

- `1 <= s.length <= 5 * 10^5`
- `s` consists of uppercase and lowercase English letters and digits.

---

## Complexity Analysis

- **Time Complexity**: `O(N) Bucket Sort or O(N log K)`
- **Space Complexity**: `O(N)`
