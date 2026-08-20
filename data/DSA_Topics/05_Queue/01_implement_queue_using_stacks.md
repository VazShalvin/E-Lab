# 1. Implement Queue using Stacks

**Topic**: Queue  
**Difficulty**: Easy  
**Tags**: Stack, Design, Queue

---

## Problem Statement

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:
- `void push(int x)` Pushes element x to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

---

## Input & Output Format

- **Input**: Operations and arguments.
- **Output**: Outputs corresponding to operations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2]
myQueue.peek();  // return 1
myQueue.pop();   // return 1, queue is [2]
myQueue.empty(); // return false
```

**Output:**
```text
[null, null, null, 1, 1, false]
```

**Explanation:**
FIFO behavior achieved using two stacks.

### Example 2

**Input:**
```text
MyQueue myQueue = new MyQueue();
myQueue.push(10);
myQueue.empty();
```

**Output:**
```text
[null, null, false]
```

**Explanation:**
Queue is not empty.

### Example 3

**Input:**
```text
MyQueue myQueue = new MyQueue();
myQueue.push(5);
myQueue.pop();
myQueue.empty();
```

**Output:**
```text
[null, null, 5, true]
```

**Explanation:**
Queue becomes empty after popping the only element.

---

## Constraints

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.
- All calls to `pop` and `peek` are valid.

---

## Complexity Analysis

- **Time Complexity**: `O(1) amortized for pop/peek, O(1) for push`
- **Space Complexity**: `O(N)`
