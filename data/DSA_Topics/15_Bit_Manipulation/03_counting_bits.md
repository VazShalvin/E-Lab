# 3. Counting Bits

**Topic**: Bit Manipulation  
**Difficulty**: Easy  
**Tags**: Dynamic Programming, Bit Manipulation

---

## Problem Statement

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the **number of `1`'s** in the binary representation of `i`.

Can you do it in linear time `O(n)` and possibly in a single pass without using any built-in functions?

---

## Input & Output Format

- **Input**: An integer `n`.
- **Output**: An array of integers `ans`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
n = 2
```

**Output:**
```text
[0, 1, 1]
```

**Explanation:**
0 --> 0
1 --> 1
2 --> 10 (one 1)

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
[0, 1, 1, 2, 1, 2]
```

**Explanation:**
0->0, 1->1, 2->1, 3->2, 4->1, 5->2.

### Example 3

**Input:**
```text
n = 0
```

**Output:**
```text
[0]
```

**Explanation:**
0 bits for 0.

---

## Constraints

- `0 <= n <= 10^5`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
