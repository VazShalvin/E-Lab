# 3. Hand of Straights

**Topic**: Greedy  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Greedy, Sorting

---

## Problem Statement

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array `hand` where `hand[i]` is the value written on the `i-th` card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

---

## Input & Output Format

- **Input**: An array of integers `hand` and an integer `groupSize`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
```

**Output:**
```text
true
```

**Explanation:**
Alice's hand can be rearranged as [1, 2, 3], [2, 3, 4], [6, 7, 8].

### Example 2

**Input:**
```text
hand = [1, 2, 3, 4, 5], groupSize = 4
```

**Output:**
```text
false
```

**Explanation:**
Alice cannot rearrange cards into groups of 4.

### Example 3

**Input:**
```text
hand = [8, 10, 12], groupSize = 3
```

**Output:**
```text
false
```

**Explanation:**
Cards are not consecutive.

---

## Constraints

- `1 <= hand.length <= 10^4`
- `0 <= hand[i] <= 10^9`
- `1 <= groupSize <= hand.length`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
