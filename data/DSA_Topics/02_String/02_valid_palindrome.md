# 2. Valid Palindrome

**Topic**: String  
**Difficulty**: Easy  
**Tags**: Two Pointers, String

---

## Problem Statement

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "A man, a plan, a canal: Panama"
```

**Output:**
```text
true
```

**Explanation:**
"amanaplanacanalpanama" is a palindrome.

### Example 2

**Input:**
```text
s = "race a car"
```

**Output:**
```text
false
```

**Explanation:**
"raceacar" is not a palindrome.

### Example 3

**Input:**
```text
s = " "
```

**Output:**
```text
true
```

**Explanation:**
s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

---

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
