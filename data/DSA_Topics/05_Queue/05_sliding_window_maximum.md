# 5. Sliding Window Maximum (Monotonic Queue)

**Topic**: Queue  
**Difficulty**: Hard  
**Tags**: Array, Queue, Sliding Window, Monotonic Queue

---

## Problem Statement

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

---

## Input & Output Format

- **Input**: An array of integers `nums` and an integer `k`.
- **Output**: An array of integers representing maximums in each sliding window.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
```

**Output:**
```text
[3, 3, 5, 5, 6, 7]
```

**Explanation:**
Window [1, 3, -1] -> max 3
Window [3, -1, -3] -> max 3
Window [-1, -3, 5] -> max 5
Window [-3, 5, 3] -> max 5
Window [5, 3, 6] -> max 6
Window [3, 6, 7] -> max 7

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
Single element array window max is 1.

### Example 3

**Input:**
```text
nums = [9, 11], k = 2
```

**Output:**
```text
[11]
```

**Explanation:**
Window of size 2 is [9, 11], max is 11.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(k)`
