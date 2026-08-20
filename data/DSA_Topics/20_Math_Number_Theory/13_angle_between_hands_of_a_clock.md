# 13. Angle Between Hands of a Clock

**Topic**: Math & Number Theory  
**Difficulty**: Medium  
**Tags**: Math

---

## Problem Statement

Given two numbers, `hour` and `minutes`, return the smaller angle (in degrees) formed between the `hour` and the `minute` hand.

Answers within `10^-5` of the actual value will be accepted as correct.

---

## Input & Output Format

- **Input**: Two integers `hour` and `minutes`.
- **Output**: A double representing the smaller angle in degrees `[0, 180]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
hour = 12, minutes = 30
```

**Output:**
```text
165
```

**Explanation:**
Hour hand is at 360/12 * 12 + 30 * 0.5 = 15 deg. Minute hand is at 30 * 6 = 180 deg. |180 - 15| = 165.

### Example 2

**Input:**
```text
hour = 3, minutes = 30
```

**Output:**
```text
75
```

**Explanation:**
Angle between hands is 75 degrees.

### Example 3

**Input:**
```text
hour = 3, minutes = 15
```

**Output:**
```text
7.5
```

**Explanation:**
Angle between hands is 7.5 degrees.

---

## Constraints

- `1 <= hour <= 12`
- `0 <= minutes <= 59`

---

## Complexity Analysis

- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`
