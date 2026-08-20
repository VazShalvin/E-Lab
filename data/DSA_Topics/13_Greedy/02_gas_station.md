# 2. Gas Station (Circuit Tour)

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: Array, Greedy

---

## Problem Statement

There are `n` gas stations along a circular route, where the amount of gas at the `i-th` station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i-th` station to its next `(i + 1)-th` station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is **guaranteed to be unique**.

---

## Input & Output Format

- **Input**: Two integer arrays `gas` and `cost`.
- **Output**: An integer starting station index, or `-1`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
```

**Output:**
```text
3
```

**Explanation:**
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Cost is 1. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Cost is 2. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Cost is 3. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Cost is 4. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.

### Example 2

**Input:**
```text
gas = [2, 3, 4], cost = [3, 4, 3]
```

**Output:**
```text
-1
```

**Explanation:**
Total gas (9) < total cost (10), impossible to complete circuit.

### Example 3

**Input:**
```text
gas = [5, 1, 2, 3, 4], cost = [4, 4, 1, 5, 1]
```

**Output:**
```text
4
```

**Explanation:**
Starting at station 4 completes circuit.

---

## Constraints

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
