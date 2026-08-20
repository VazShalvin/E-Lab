# 2. Top K Frequent Elements

**Topic**: Heap / Priority Queue  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Divide and Conquer, Sorting, Heap, Bucket Sort

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `k`.
- **Output**: An array of `k` integers.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 1, 1, 2, 2, 3], k = 2
```

**Output:**
```text
[1, 2]
```

**Explanation:**
1 appears 3 times, 2 appears 2 times, 3 appears 1 time.

### Example 2

**Input:**
```text
nums = [1], k = 1
```

**Output:**
```text
[1]
```

**Explanation:**
1 is the only frequent element.

### Example 3

**Input:**
```text
nums = [4, 4, 4, 6, 6, 7, 7, 7, 7], k = 1
```

**Output:**
```text
[7]
```

**Explanation:**
7 has frequency 4.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

---

## Complexity Analysis

- **Time Complexity**: `O(N log k) or O(N) Bucket Sort`
- **Space Complexity**: `O(N)`
