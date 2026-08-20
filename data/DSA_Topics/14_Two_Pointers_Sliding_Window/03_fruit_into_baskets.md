# 3. Fruit Into Baskets

**Topic**: Two Pointers & Sliding Window  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, Sliding Window

---

## Problem Statement

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the **type** of fruit the `i-th` tree produces.

You have **two baskets**, and each basket can only hold a **single type** of fruit. There is no limit on the amount of fruit each basket can hold.

Starting from any tree of your choice, you must pick **exactly one fruit** from every tree while moving to the right. Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Return the **maximum number** of fruits you can pick.

---

## Input & Output Format

- **Input**: An array of integers `fruits`.
- **Output**: An integer representing the maximum fruits picked.

---

## Sample Test Cases

### Example 1

**Input:**
```text
fruits = [1, 2, 1]
```

**Output:**
```text
3
```

**Explanation:**
We can pick from all 3 trees.

### Example 2

**Input:**
```text
fruits = [0, 1, 2, 2]
```

**Output:**
```text
3
```

**Explanation:**
We can pick from [1, 2, 2].

### Example 3

**Input:**
```text
fruits = [1, 2, 3, 2, 2]
```

**Output:**
```text
4
```

**Explanation:**
We can pick from [2, 3, 2, 2].

---

## Constraints

- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
