# 2. Min Stack

**Topic**: Stack  
**Difficulty**: Medium  
**Tags**: Stack, Design

---

## Problem Statement

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

---

## Input & Output Format

- **Input**: List of operations and arguments.
- **Output**: List of outputs corresponding to calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Output:**
```text
[null, null, null, null, -3, null, 0, -2]
```

**Explanation:**
Maintains min tracking at each stack level.

### Example 2

**Input:**
```text
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.getMin();
```

**Output:**
```text
[null, null, null, 1]
```

**Explanation:**
Minimum is 1.

### Example 3

**Input:**
```text
MinStack minStack = new MinStack();
minStack.push(5);
minStack.top();
```

**Output:**
```text
[null, null, 5]
```

**Explanation:**
Top element is 5.

---

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

---

## Complexity Analysis

- **Time Complexity**: `O(1) for all methods`
- **Space Complexity**: `O(N)`
