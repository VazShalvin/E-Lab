# 8. Elimination Game

**Topic**: Recursion  
**Difficulty**: Medium  
**Tags**: Math, Recursion

---

## Problem Statement

You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:
- Starting from left to right, remove the first number and every other number even after that until you reach the end of the list.
- Repeat the previous step, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
- Keep alternating the steps from left to right and right to left until a single number remains.

Given the integer `n`, return the last number that remains in `arr`.

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: An integer representing the last remaining number.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 9
```

**Output:**
```text
6
```

**Explanation:**
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Left to right: [2, 4, 6, 8]
Right to left: [2, 6]
Left to right: [6]
Returns 6.

### Example 2

**Input:**
```text
n = 1
```

**Output:**
```text
1
```

**Explanation:**
Single number 1.

### Example 3

**Input:**
```text
n = 4
```

**Output:**
```text
2
```

**Explanation:**
[1, 2, 3, 4] -> [2, 4] -> [2].

---

## Constraints

- `1 <= n <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(log N) or O(1)`
