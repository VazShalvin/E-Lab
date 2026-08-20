# 8. Lemonade Change

**Topic**: Greedy  
**Difficulty**: Easy  
**Tags**: Array, Greedy

---

## Problem Statement

At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time. Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.

Note that you do not have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the `i-th` customer pays, return `true` if you can provide every customer with the correct change, or `false` otherwise.

---

## Input & Output Format

- **Input**: An array of integers `bills`.
- **Output**: A boolean (`true` or `false`).

---

## Sample Test Cases

### Example 1

**Input:**
```text
bills = [5, 5, 5, 10, 20]
```

**Output:**
```text
true
```

**Explanation:**
Collect three $5 bills, give $5 change for $10, and give one $10 and one $5 change for $20.

### Example 2

**Input:**
```text
bills = [5, 5, 10, 10, 20]
```

**Output:**
```text
false
```

**Explanation:**
For the last $20 bill, you cannot provide $15 change because you only have two $10 bills.

### Example 3

**Input:**
```text
bills = [5, 5, 5, 5, 20, 20, 5, 5, 5, 5]
```

**Output:**
```text
false
```

**Explanation:**
Cannot make change for second $20 bill.

---

## Constraints

- `1 <= bills.length <= 10^5`
- `bills[i]` is either `5`, `10`, or `20`.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
