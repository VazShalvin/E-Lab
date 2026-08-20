# 4. Daily Temperatures

**Topic**: Stack  
**Difficulty**: Medium  
**Tags**: Array, Stack, Monotonic Stack

---

## Problem Statement

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

---

## Input & Output Format

- **Input**: An array of integers `temperatures`.
- **Output**: An array of integers `answer`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
```

**Output:**
```text
[1, 1, 4, 2, 1, 1, 0, 0]
```

**Explanation:**
For day 0 (73), day 1 (74) is warmer -> wait 1 day.
For day 2 (75), day 6 (76) is warmer -> wait 4 days.

### Example 2

**Input:**
```text
temperatures = [30, 40, 50, 60]
```

**Output:**
```text
[1, 1, 1, 0]
```

**Explanation:**
Each day is strictly warmer than the previous day.

### Example 3

**Input:**
```text
temperatures = [30, 60, 90]
```

**Output:**
```text
[1, 1, 0]
```

**Explanation:**
Day 0 waits 1 day, day 1 waits 1 day, day 2 has no warmer day.

---

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
