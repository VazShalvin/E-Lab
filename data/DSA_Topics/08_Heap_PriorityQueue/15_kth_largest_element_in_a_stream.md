# 15. Kth Largest Element in a Stream

**Topic**: Heap / Priority Queue  
**Difficulty**: Easy  
**Tags**: Tree, Design, Binary Search Tree, Heap, Data Stream

---

## Problem Statement

Design a class to find the `k-th` largest element in a stream. Note that it is the `k-th` largest element in the sorted order, not the `k-th` distinct element.

Implement `KthLargest` class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `k-th` largest element in the stream.

---

## Input & Output Format

- **Input**: Constructor args and sequential `add(val)` calls.
- **Output**: Array of returned values for each add call.

---

## Sample Test Cases

### Example 1

**Input:**
```text
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

**Output:**
```text
[null, 4, 5, 5, 8, 8]
```

**Explanation:**
Min-heap of fixed size k = 3 keeps top 3 largest elements; heap top is the 3rd largest.

### Example 2

**Input:**
```text
KthLargest kl = new KthLargest(1, []); kl.add(3);
```

**Output:**
```text
[null, 3]
```

**Explanation:**
1st largest is 3.

### Example 3

**Input:**
```text
kl.add(5); kl.add(1);
```

**Output:**
```text
[5, 5]
```

**Explanation:**
Returns 5 for both.

---

## Constraints

- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- `-10^4 <= nums[i], val <= 10^4`
- At most `10^4` calls will be made to `add`.

---

## Complexity Analysis

- **Time Complexity**: `O(log k) per add`
- **Space Complexity**: `O(k)`
