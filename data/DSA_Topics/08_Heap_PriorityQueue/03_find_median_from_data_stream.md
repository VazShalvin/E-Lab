# 3. Find Median from Data Stream

**Topic**: Heap / Priority Queue  
**Difficulty**: Hard  
**Tags**: Two Pointers, Design, Sorting, Heap, Data Stream

---

## Problem Statement

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

Implement the `MedianFinder` class:
- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far.

---

## Input & Output Format

- **Input**: Method calls and parameters.
- **Output**: Outputs corresponding to findMedian calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

**Output:**
```text
[null, null, null, 1.5, null, 2.0]
```

**Explanation:**
Maintains max-heap for lower half and min-heap for upper half.

### Example 2

**Input:**
```text
mf.addNum(5); mf.findMedian();
```

**Output:**
```text
[null, 5.0]
```

**Explanation:**
Single number median is itself.

### Example 3

**Input:**
```text
mf.addNum(1); mf.addNum(3); mf.findMedian();
```

**Output:**
```text
[null, null, 2.0]
```

**Explanation:**
(1 + 3) / 2 = 2.0.

---

## Constraints

- `-10^5 <= num <= 10^5`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

---

## Complexity Analysis

- **Time Complexity**: `O(log N) addNum, O(1) findMedian`
- **Space Complexity**: `O(N)`
