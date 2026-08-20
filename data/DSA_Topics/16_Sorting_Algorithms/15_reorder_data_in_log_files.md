# 15. Reorder Data in Log Files (Custom Key Sorting)

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, String, Sorting

---

## Problem Statement

You are given an array of `logs`. Each log is a space-delimited string of words, where the first word is the **identifier**.

There are two types of logs:
- **Letter-logs**: All words (except the identifier) consist of lowercase English letters.
- **Digit-logs**: All words (except the identifier) consist of digits.

Reorder these logs so that:
1. The **letter-logs** come before all **digit-logs**.
2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3. The digit-logs maintain their relative order.

---

## Input & Output Format

- **Input**: An array of strings `logs`.
- **Output**: An array of reordered log strings.

---

## Sample Test Cases

### Example 1

**Input:**
```text
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
```

**Output:**
```text
["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
```

**Explanation:**
Letter logs sorted by content then id; digit logs keep relative order.

### Example 2

**Input:**
```text
logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
```

**Output:**
```text
["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
```

**Explanation:**
Properly partitioned and sorted.

### Example 3

**Input:**
```text
logs = ["let1 a b", "let2 a b"]
```

**Output:**
```text
["let1 a b", "let2 a b"]
```

**Explanation:**
Tie in content broken by identifier.

---

## Constraints

- `1 <= logs.length <= 100`
- `3 <= logs[i].length <= 100`
- All the tokens in `logs[i]` are separated by a **single space**.

---

## Complexity Analysis

- **Time Complexity**: `O(M * N log N) where M is max log length`
- **Space Complexity**: `O(M * N)`
