# 11. Maximum Units on a Truck

**Topic**: Greedy  
**Difficulty**: Easy  
**Tags**: Array, Greedy, Sorting

---

## Problem Statement

You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxes_i, numberOfUnitsPerBox_i]`.

You are also given an integer `truckSize`, which is the **maximum number of boxes** that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed `truckSize`.

Return the **maximum total number of units** that can be put on the truck.

---

## Input & Output Format

- **Input**: A 2D array `boxTypes` and an integer `truckSize`.
- **Output**: An integer representing maximum units.

---

## Sample Test Cases

### Example 1

**Input:**
```text
boxTypes = [[1, 3], [2, 2], [3, 1]], truckSize = 4
```

**Output:**
```text
8
```

**Explanation:**
1 box of 3 units + 2 boxes of 2 units + 1 box of 1 unit = 3 + 4 + 1 = 8 units.

### Example 2

**Input:**
```text
boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]], truckSize = 10
```

**Output:**
```text
91
```

**Explanation:**
5*10 + 3*9 + 2*7 = 50 + 27 + 14 = 91 units.

### Example 3

**Input:**
```text
boxTypes = [[1, 1]], truckSize = 0
```

**Output:**
```text
0
```

**Explanation:**
Truck size 0 holds 0 units.

---

## Constraints

- `1 <= boxTypes.length <= 1000`
- `1 <= numberOfBoxes_i, numberOfUnitsPerBox_i <= 1000`
- `1 <= truckSize <= 10^6`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(1)`
