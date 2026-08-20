# 13. Moving Average from Data Stream

**Topic**: Queue  
**Difficulty**: Easy  
**Tags**: Array, Design, Queue, Data Stream

---

## Problem Statement

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the `MovingAverage` class:
- `MovingAverage(int size)` Initializes the object with the size of the window `size`.
- `double next(int val)` Returns the moving average of the last `size` values of the stream.

---

## Input & Output Format

- **Input**: Calls to `next(val)`.
- **Output**: Floating point moving average.

---

## Sample Test Cases

### Example 1

**Input:**
```text
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
```

**Output:**
```text
[null, 1.0, 5.5, 4.66667, 6.0]
```

**Explanation:**
When elements exceed capacity 3, oldest element 1 is dequeued.

### Example 2

**Input:**
```text
MovingAverage ma = new MovingAverage(1);
ma.next(4); // 4.0
ma.next(8); // 8.0
```

**Output:**
```text
[null, 4.0, 8.0]
```

**Explanation:**
Window size 1 returns the latest value.

### Example 3

**Input:**
```text
MovingAverage ma = new MovingAverage(2);
ma.next(2); // 2.0
ma.next(4); // 3.0
```

**Output:**
```text
[null, 2.0, 3.0]
```

**Explanation:**
(2+4)/2 = 3.0.

---

## Constraints

- `1 <= size <= 1000`
- `-10^5 <= val <= 10^5`
- At most `10^4` calls will be made to `next`.

---

## Complexity Analysis

- **Time Complexity**: `O(1) per call`
- **Space Complexity**: `O(size)`
