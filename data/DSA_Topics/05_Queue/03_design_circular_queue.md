# 3. Design Circular Queue

**Topic**: Queue  
**Difficulty**: Medium  
**Tags**: Array, Linked List, Design, Queue

---

## Problem Statement

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO principle and the last position is connected back to the first position to make a circle.

Implement the `MyCircularQueue` class with methods `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, `isFull`.

---

## Input & Output Format

- **Input**: Operations and arguments.
- **Output**: Outputs corresponding to circular queue operations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
```

**Output:**
```text
[null, true, true, true, false, 3, true, true, true, 4]
```

**Explanation:**
Demonstrates wrap-around behavior after dequeuing.

### Example 2

**Input:**
```text
MyCircularQueue q = new MyCircularQueue(2);
q.isEmpty(); // true
q.enQueue(10); // true
q.Front(); // 10
```

**Output:**
```text
[null, true, true, 10]
```

**Explanation:**
Basic inspection on circular queue.

### Example 3

**Input:**
```text
MyCircularQueue q = new MyCircularQueue(1);
q.enQueue(5); // true
q.isFull(); // true
q.enQueue(6); // false
```

**Output:**
```text
[null, true, true, false]
```

**Explanation:**
Capacity 1 becomes full immediately.

---

## Constraints

- `1 <= k <= 1000`
- `0 <= value <= 1000`
- At most `3000` calls will be made to `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull`.

---

## Complexity Analysis

- **Time Complexity**: `O(1) for all methods`
- **Space Complexity**: `O(K)`
