# 9. Letter Combinations of a Phone Number

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Backtracking

---

## Problem Statement

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
- 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"

---

## Input & Output Format

- **Input**: A string of digits `digits`.
- **Output**: An array of combination strings.

---

## Sample Test Cases

### Example 1

**Input:**
```text
digits = "23"
```

**Output:**
```text
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

**Explanation:**
All 3 * 3 = 9 combinations.

### Example 2

**Input:**
```text
digits = ""
```

**Output:**
```text
[]
```

**Explanation:**
Empty input produces empty array.

### Example 3

**Input:**
```text
digits = "2"
```

**Output:**
```text
["a", "b", "c"]
```

**Explanation:**
Single digit yields 3 choices.

---

## Constraints

- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

---

## Complexity Analysis

- **Time Complexity**: `O(4^N)`
- **Space Complexity**: `O(N)`
