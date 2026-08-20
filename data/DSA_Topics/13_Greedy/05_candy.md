# 5. Candy Distribution

**Topic**: Greedy  
**Difficulty**: Hard  
**Tags**: Array, Greedy

---

## Problem Statement

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

---

## Input & Output Format

- **Input**: An array of integers `ratings`.
- **Output**: An integer representing the minimum number of candies.

---

## Sample Test Cases

### Example 1

**Input:**
```text
ratings = [1, 0, 2]
```

**Output:**
```text
5
```

**Explanation:**
You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

### Example 2

**Input:**
```text
ratings = [1, 2, 2]
```

**Output:**
```text
4
```

**Explanation:**
You can allocate to the first, second and third child with 1, 2, 1 candies respectively.

### Example 3

**Input:**
```text
ratings = [1, 3, 2, 2, 1]
```

**Output:**
```text
7
```

**Explanation:**
Candies: [1, 2, 1, 2, 1] sum = 7.

---

## Constraints

- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
