# 10. Dota2 Senate

**Topic**: Queue  
**Difficulty**: Medium  
**Tags**: String, Greedy, Queue

---

## Problem Statement

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:
1. **Ban one senator's right**: A senator can make another senator lose all his rights in this and all following rounds.
2. **Announce the victory**: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string `senate` representing each senator's party affiliation, predict which party will finally announce the victory.

---

## Input & Output Format

- **Input**: A string `senate` containing `'R'` and `'D'`.
- **Output**: String `"Radiant"` or `"Dire"`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
senate = "RD"
```

**Output:**
```text
"Radiant"
```

**Explanation:**
The first senator from Radiant can ban the next senator from Dire's right in the first round. And the second senator can't exercise any rights anymore. So Radiant will win.

### Example 2

**Input:**
```text
senate = "RDD"
```

**Output:**
```text
"Dire"
```

**Explanation:**
The first senator from Radiant bans the first Dire. The second Dire senator bans Radiant. In round 2, Dire senator announces victory.

### Example 3

**Input:**
```text
senate = "RRDDD"
```

**Output:**
```text
"Radiant"
```

**Explanation:**
Radiant senators ban Dire senators efficiently to secure victory.

---

## Constraints

- `n == senate.length`
- `1 <= n <= 10^4`
- `senate[i]` is either `'R'` or `'D'`.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
