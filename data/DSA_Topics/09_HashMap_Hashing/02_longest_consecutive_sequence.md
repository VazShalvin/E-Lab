# 2. Longest Consecutive Sequence

**Topic**: HashMap / Hashing  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Union Find

---

## Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the sequence length.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [100, 4, 200, 1, 3, 2]
```

**Output:**
```text
4
```

**Explanation:**
The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

### Example 2

**Input:**
```text
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
```

**Output:**
```text
9
```

**Explanation:**
The sequence is 0, 1, 2, 3, 4, 5, 6, 7, 8 with length 9.

### Example 3

**Input:**
```text
nums = []
```

**Output:**
```text
0
```

**Explanation:**
Empty array returns 0.

---

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
