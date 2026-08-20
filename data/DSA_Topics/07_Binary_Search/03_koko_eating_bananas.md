# 3. Koko Eating Bananas

**Topic**: Binary Search  
**Difficulty**: Medium  
**Tags**: Array, Binary Search

---

## Problem Statement

Koko loves to eat bananas. There are `n` piles of bananas, the `i-th` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

---

## Input & Output Format

- **Input**: An array of integers `piles` and an integer `h`.
- **Output**: An integer representing minimum speed `k`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
piles = [3, 6, 7, 11], h = 8
```

**Output:**
```text
4
```

**Explanation:**
At speed 4: ceil(3/4) + ceil(6/4) + ceil(7/4) + ceil(11/4) = 1 + 2 + 2 + 3 = 8 hours.

### Example 2

**Input:**
```text
piles = [30, 11, 23, 4, 20], h = 5
```

**Output:**
```text
30
```

**Explanation:**
At speed 30, she eats each pile in 1 hour (5 hours total).

### Example 3

**Input:**
```text
piles = [30, 11, 23, 4, 20], h = 6
```

**Output:**
```text
23
```

**Explanation:**
At speed 23, hours = 2 + 1 + 1 + 1 + 1 = 6 hours.

---

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

---

## Complexity Analysis

- **Time Complexity**: `O(N log(max(piles)))`
- **Space Complexity**: `O(1)`
