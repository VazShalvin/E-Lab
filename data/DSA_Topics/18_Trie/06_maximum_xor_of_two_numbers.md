# 6. Maximum XOR of Two Numbers in an Array (Bitwise Trie)

**Topic**: Trie  
**Difficulty**: Medium  
**Tags**: Array, Bit Manipulation, Trie

---

## Problem Statement

Given an integer array `nums`, return the maximum result of `nums[i] XOR nums[j]`, where `0 <= i <= j < n`.

You must solve it in `O(N)` time complexity using a 32-bit Binary Trie.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the maximum XOR value.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [3, 10, 5, 25, 2, 8]
```

**Output:**
```text
28
```

**Explanation:**
The maximum result is 5 XOR 25 = 28.

### Example 2

**Input:**
```text
nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
```

**Output:**
```text
127
```

**Explanation:**
Maximum XOR formed is 127.

### Example 3

**Input:**
```text
nums = [0]
```

**Output:**
```text
0
```

**Explanation:**
0 XOR 0 = 0.

---

## Constraints

- `1 <= nums.length <= 2 * 10^5`
- `0 <= nums[i] <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(32 * N) = O(N)`
- **Space Complexity**: `O(32 * N) = O(N)`
