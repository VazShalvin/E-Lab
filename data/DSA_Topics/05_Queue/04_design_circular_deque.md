# 4. Design Circular Deque

**Topic**: Queue  
**Difficulty**: Medium  
**Tags**: Array, Linked List, Design, Queue

---

## Problem Statement

Design your implementation of the circular double-ended queue (deque).

Implement the `MyCircularDeque` class with operations: `insertFront`, `insertLast`, `deleteFront`, `deleteLast`, `getFront`, `getRear`, `isEmpty`, `isFull`.

---

## Input & Output Format

- **Input**: Operations and arguments.
- **Output**: Outputs corresponding to deque operations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, queue is full
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4
```

**Output:**
```text
[null, true, true, true, false, 2, true, true, true, 4]
```

**Explanation:**
Supports insertion and deletion from both ends.

### Example 2

**Input:**
```text
MyCircularDeque dq = new MyCircularDeque(2);
dq.insertFront(7);
dq.getFront();
```

**Output:**
```text
[null, true, 7]
```

**Explanation:**
Inserts 7 at front and reads 7.

### Example 3

**Input:**
```text
MyCircularDeque dq = new MyCircularDeque(1);
dq.isEmpty();
```

**Output:**
```text
[null, true]
```

**Explanation:**
Newly created deque is empty.

---

## Constraints

- `1 <= k <= 1000`
- `0 <= value <= 1000`
- At most `2000` calls will be made to methods.

---

## Complexity Analysis

- **Time Complexity**: `O(1) for all operations`
- **Space Complexity**: `O(K)`
