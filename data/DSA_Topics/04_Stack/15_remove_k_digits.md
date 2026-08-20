# 15. Remove K Digits

**Topic**: Stack  
**Difficulty**: Medium  
**Tags**: String, Stack, Greedy, Monotonic Stack

---

## Problem Statement

Given string `num` representing a non-negative integer `num`, and an integer `k`, return the smallest possible integer after removing `k` digits from `num`.

---

## Input & Output Format

- **Input**: A string `num` and an integer `k`.
- **Output**: A string representing the smallest integer without leading zeroes.

---

## Sample Test Cases

### Example 1

**Input:**
```text
num = "1432219", k = 3
```

**Output:**
```text
"1219"
```

**Explanation:**
Remove digits 4, 3, and 2 to form the smallest number 1219.

### Example 2

**Input:**
```text
num = "10200", k = 1
```

**Output:**
```text
"200"
```

**Explanation:**
Remove the leading 1 to get "0200" -> "200".

### Example 3

**Input:**
```text
num = "10", k = 2
```

**Output:**
```text
"0"
```

**Explanation:**
Remove all digits, returning "0".

---

## Constraints

- `1 <= k <= num.length <= 10^5`
- `num` consists of only digits.
- `num` does not have any leading zeros except for the zero itself.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
