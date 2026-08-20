# 7. Maximum XOR With an Element From Array (Offline Queries + Trie)

**Topic**: Trie  
**Difficulty**: Hard  
**Tags**: Array, Bit Manipulation, Trie

---

## Problem Statement

You are given an array `nums` consisting of non-negative integers. You are also given a `queries` array, where `queries[j] = [x_j, m_j]`.

The answer to the `j-th` query is the maximum bitwise `XOR` value of `x_j` with any element of `nums` that does not exceed `m_j`. In other words, the answer is `max(nums[i] XOR x_j)` for all `i` such that `nums[i] <= m_j`. If all elements in `nums` are larger than `m_j`, then the answer is `-1`.

Return an integer array `answer` where `answer.length == queries.length`.

---

## Input & Output Format

- **Input**: An array `nums` and a 2D array `queries`.
- **Output**: An array of integers `answer`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [0, 1, 2, 3, 4], queries = [[3, 1], [1, 3], [5, 6]]
```

**Output:**
```text
[3, 3, 7]
```

**Explanation:**
1) 0 and 1 are <= 1. max(3 XOR 0, 3 XOR 1) = 3.
2) 0, 1, 2, 3 are <= 3. max(1 XOR 0, 1 XOR 1, 1 XOR 2, 1 XOR 3) = 3.
3) All elements are <= 6. max(5 XOR 0, ... 5 XOR 4) = 7.

### Example 2

**Input:**
```text
nums = [5, 2, 4, 6, 6, 3], queries = [[12, 4], [8, 1], [6, 3]]
```

**Output:**
```text
[15, -1, 5]
```

**Explanation:**
For [8, 1], no elements <= 1 exist, so -1.

### Example 3

**Input:**
```text
nums = [1], queries = [[1, 0]]
```

**Output:**
```text
[-1]
```

**Explanation:**
No element <= 0.

---

## Constraints

- `1 <= nums.length, queries.length <= 10^5`
- `queries[j].length == 2`
- `0 <= nums[i], x_j, m_j <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N + Q log Q + (N + Q) * 32)`
- **Space Complexity**: `O(32 * N + Q)`
