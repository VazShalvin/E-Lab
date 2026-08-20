# 8. Reveal Cards In Increasing Order

**Topic**: Queue  
**Difficulty**: Medium  
**Tags**: Array, Queue, Sorting, Simulation

---

## Problem Statement

You are given an integer array `deck`. There is a deck of cards where every card has a unique integer. The integer on the `i-th` card is `deck[i]`.

You can order the deck in any order you want. Initially, all the cards start face down in one pile.

You will do the following steps repeatedly until all cards are revealed:
1. Take the top card of the deck, reveal it, and take it out of the pile.
2. If there are still cards in the pile then put the next top card of the deck at the bottom of the pile.
3. If there are still unrevealed cards, go back to step 1. Otherwise, stop.

Return an ordering of the deck that would reveal the cards in increasing order.

---

## Input & Output Format

- **Input**: An array of integers `deck`.
- **Output**: An array of integers representing the arranged deck.

---

## Sample Test Cases

### Example 1

**Input:**
```text
deck = [17, 13, 11, 2, 3, 5, 7]
```

**Output:**
```text
[2, 13, 3, 11, 5, 17, 7]
```

**Explanation:**
Simulating the reveal steps yields [2, 3, 5, 7, 11, 13, 17] in perfectly increasing order.

### Example 2

**Input:**
```text
deck = [1, 1000]
```

**Output:**
```text
[1, 1000]
```

**Explanation:**
Reveal 1, shift 1000, reveal 1000.

### Example 3

**Input:**
```text
deck = [5, 4, 3, 2, 1]
```

**Output:**
```text
[1, 5, 2, 4, 3]
```

**Explanation:**
Correctly reveals 1, 2, 3, 4, 5.

---

## Constraints

- `1 <= deck.length <= 1000`
- `1 <= deck[i] <= 10^6`
- All the values of `deck` are unique.

---

## Complexity Analysis

- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
