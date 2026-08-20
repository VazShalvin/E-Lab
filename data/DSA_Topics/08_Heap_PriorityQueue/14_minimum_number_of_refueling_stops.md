# 14. Minimum Number of Refueling Stops

**Topic**: Heap / Priority Queue  
**Difficulty**: Hard  
**Tags**: Array, Dynamic Programming, Greedy, Heap

---

## Problem Statement

A car travels from a starting position to a destination which is `target` miles east of the starting position. The car starts with `startFuel` liters of gas. It uses 1 liter of gas per 1 mile that it drives.

There are gas stations along the way represented as an integer array `stations` where `stations[i] = [position_i, fuel_i]`.

Return the minimum number of refueling stops the car must make to reach its destination. If it cannot reach the destination, return `-1`.

---

## Input & Output Format

- **Input**: Integers `target` and `startFuel`, and a 2D array `stations`.
- **Output**: An integer count of refueling stops, or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
target = 1, startFuel = 1, stations = []
```

**Output:**
```text
0
```

**Explanation:**
We can reach the target without refueling.

### Example 2

**Input:**
```text
target = 100, startFuel = 1, stations = [[10, 100]]
```

**Output:**
```text
-1
```

**Explanation:**
We cannot reach station 1 at position 10 with only 1 liter of gas.

### Example 3

**Input:**
```text
target = 100, startFuel = 10, stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
```

**Output:**
```text
2
```

**Explanation:**
Refuel at position 10 (fuel 60) and position 60 (fuel 40).

---

## Constraints

- `1 <= target, startFuel <= 10^9`
- `0 <= stations.length <= 500`
- `1 <= position_i < position_i+1 < target`
- `1 <= fuel_i <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
