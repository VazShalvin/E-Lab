# 12. Count and Say

**Topic**: String  
**Difficulty**: Medium  
**Tags**: String

---

## Problem Statement

The **count-and-say** sequence is a sequence of digit strings defined by the recursive formula:
- `countAndSay(1) = "1"`
- `countAndSay(n)` is the run-length encoding of `countAndSay(n - 1)`.

Given a positive integer `n`, return the `n-th` term of the count-and-say sequence.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: A string representing the `n-th` count-and-say term.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 1
```

**Output:**
```text
"1"
```

**Explanation:**
Base case.

### Example 2

**Input:**
```text
n = 4
```

**Output:**
```text
"1211"
```

**Explanation:**
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1s = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "1211"

### Example 3

**Input:**
```text
n = 5
```

**Output:**
```text
"111221"
```

**Explanation:**
Saying "1211" -> "111221".

---

## Constraints

- `1 <= n <= 30`

---

## Complexity Analysis

- **Time Complexity**: `O(2^N)`
- **Space Complexity**: `O(2^N)`
