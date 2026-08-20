# 11. Smallest Range Covering Elements from K Lists

**Topic**: Heap / Priority Queue  
**Difficulty**: Hard  
**Tags**: Array, Hash Table, Greedy, Sliding Window, Sorting, Heap

---

## Problem Statement

You have `k` lists of sorted integers in non-decreasing order. Find the **smallest range** `[a, b]` that includes at least one number from each of the `k` lists.

We define the range `[a, b]` is smaller than range `[c, d]` if `b - a < d - c` or `a < c` if `b - a == d - c`.

---

## Input & Output Format

- **Input**: A 2D array `nums` of `k` sorted lists.
- **Output**: An array of two integers `[a, b]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
```

**Output:**
```text
[20, 24]
```

**Explanation:**
List 1: 24, List 2: 20, List 3: 22. Range [20, 24] covers all 3 lists with length 4.

### Example 2

**Input:**
```text
nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

**Output:**
```text
[1, 1]
```

**Explanation:**
Range [1, 1] contains 1 from all three lists.

### Example 3

**Input:**
```text
nums = [[10, 10], [11, 11]]
```

**Output:**
```text
[10, 11]
```

**Explanation:**
Range [10, 11] covers both lists.

---

## Constraints

- `nums.length == k`
- `1 <= k <= 3500`
- `1 <= nums[i].length <= 50`
- `-10^5 <= nums[i][j] <= 10^5`
- `nums[i]` is sorted in non-decreasing order.

---

## Complexity Analysis

- **Time Complexity**: `O(N log k)`
- **Space Complexity**: `O(k)`
