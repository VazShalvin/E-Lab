# 6. Largest Number (Custom Comparator Sort)

**Topic**: Sorting Algorithms  
**Difficulty**: Medium  
**Tags**: Array, String, Greedy, Sorting

---

## Problem Statement

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

---

## Input & Output Format

- **Input**: An array of integers `nums`.
- **Output**: A string representing the largest number formed.

---

## Sample Test Cases

### Example 1

**Input:**
```text
nums = [10, 2]
```

**Output:**
```text
"210"
```

**Explanation:**
"210" is larger than "102".

### Example 2

**Input:**
```text
nums = [3, 30, 34, 5, 9]
```

**Output:**
```text
"9534330"
```

**Explanation:**
"9534330" is the largest concatenated number.

### Example 3

**Input:**
```text
nums = [0, 0]
```

**Output:**
```text
"0"
```

**Explanation:**
Must return "0" rather than "00".

---

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
