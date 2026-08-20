# 6. First Missing Positive (In-place Hashing)

**Topic**: HashMap / Hashing  
**Difficulty**: Hard  
**Tags**: Array, Hash Table

---

## Problem Statement

Given an unsorted integer array `nums`, return the smallest positive integer that is not present in `nums`.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: An integer representing the first missing positive.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 2, 0]
```

**Output:**
```text
3
```

**Explanation:**
Numbers in the range [1, 2] are all in the array. Smallest missing is 3.

### Example 2

**Input:**
```text
nums = [3, 4, -1, 1]
```

**Output:**
```text
2
```

**Explanation:**
1 is in the array, but 2 is missing.

### Example 3

**Input:**
```text
nums = [7, 8, 9, 11, 12]
```

**Output:**
```text
1
```

**Explanation:**
Smallest positive integer 1 is missing.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
