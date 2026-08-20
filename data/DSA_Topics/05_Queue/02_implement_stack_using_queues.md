# 2. Implement Stack using Queues

**Topic**: Queue  
**Difficulty**: Easy  
**Tags**: Stack, Design, Queue

---

## Problem Statement

Implement a last-in-first-out (LIFO) stack using only standard queue operations (`push to back`, `peek/pop from front`, `size` and `is empty`).

Implement the `MyStack` class:
- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

---

## Input & Output Format

- **Input**: Operations and arguments.
- **Output**: Outputs corresponding to operations.

---

## Sample Test Cases

### Example 1

**Input:**
```text
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top();   // return 2
myStack.pop();   // return 2
myStack.empty(); // return False
```

**Output:**
```text
[null, null, null, 2, 2, false]
```

**Explanation:**
LIFO behavior achieved using standard queues.

### Example 2

**Input:**
```text
MyStack myStack = new MyStack();
myStack.push(100);
myStack.top();
```

**Output:**
```text
[null, null, 100]
```

**Explanation:**
Top element is 100.

### Example 3

**Input:**
```text
MyStack myStack = new MyStack();
myStack.empty();
```

**Output:**
```text
[null, true]
```

**Explanation:**
Initialized stack is empty.

---

## Constraints

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.

---

## Complexity Analysis

- **Time Complexity**: `O(N) for push or pop, O(1) for others`
- **Space Complexity**: `O(N)`
