# 12. Restore IP Addresses

**Topic**: Backtracking  
**Difficulty**: Medium  
**Tags**: String, Backtracking

---

## Problem Statement

A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (inclusive) and cannot have leading zeros.

Given a string `s` containing only digits, return all possible valid IP addresses that can be formed by inserting dots into `s`. You are not allowed to reorder or remove any digits in `s`. You may return the valid IP addresses in any order.

---

## Input & Output Format

- **Input**: A string `s`.
- **Output**: An array of valid IP address strings.

---

## Sample Test Cases

### Example 1

**Input:**
```text
s = "25525511135"
```

**Output:**
```text
["255.255.11.135", "255.255.111.35"]
```

**Explanation:**
Two valid partitions into 4 octets.

### Example 2

**Input:**
```text
s = "0000"
```

**Output:**
```text
["0.0.0.0"]
```

**Explanation:**
Only valid IP with four 0s.

### Example 3

**Input:**
```text
s = "101023"
```

**Output:**
```text
["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
```

**Explanation:**
All valid configurations without leading zeros in octets.

---

## Constraints

- `1 <= s.length <= 20`
- `s` consists of digits only.

---

## Complexity Analysis

- **Time Complexity**: `O(3^4) = O(1)`
- **Space Complexity**: `O(1)`
