# 4. Merge k Sorted Lists

**Topic**: LinkedList  
**Difficulty**: Hard  
**Tags**: Linked List, Divide and Conquer, Heap, Merge Sort

---

## Problem Statement

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

---

## Input & Output Format

- **Input**: An array of linked list heads `lists`.
- **Output**: Head of merged sorted linked list.

---

## Sample Test Cases

### Example 1

**Input:**
```text
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
```

**Output:**
```text
[1, 1, 2, 3, 4, 4, 5, 6]
```

**Explanation:**
Merging all 3 sorted lists into one sorted linked list.

### Example 2

**Input:**
```text
lists = []
```

**Output:**
```text
[]
```

**Explanation:**
Empty list of lists returns [].

### Example 3

**Input:**
```text
lists = [[]]
```

**Output:**
```text
[]
```

**Explanation:**
List with one empty linked list returns [].

---

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order.
- Total nodes across all lists `<= 10^4`.

---

## Complexity Analysis

- **Time Complexity**: `O(N log k)`
- **Space Complexity**: `O(k)`
