# 12. Maximum Frequency Stack

**Topic**: Queue  
**Difficulty**: Hard  
**Tags**: Hash Table, Stack, Design

---

## Problem Statement

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the `FreqStack` class:
- `FreqStack()` constructs an empty frequency stack.
- `void push(int val)` pushes an integer `val` onto the top of the stack.
- `int pop()` removes and returns the most frequent element in the stack. If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

---

## Input & Output Format

- **Input**: Operations and argument values.
- **Output**: Output list corresponding to pop calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
FreqStack freqStack = new FreqStack();
freqStack.push(5);
freqStack.push(7);
freqStack.push(5);
freqStack.push(7);
freqStack.push(4);
freqStack.push(5);
freqStack.pop(); // return 5 (frequency 3)
freqStack.pop(); // return 7 (frequency 2, tie broken by recency)
freqStack.pop(); // return 5 (frequency 2)
freqStack.pop(); // return 4 (frequency 1)
```

**Output:**
```text
[null, null, null, null, null, null, null, 5, 7, 5, 4]
```

**Explanation:**
Maintains frequency buckets for O(1) retrieval.

### Example 2

**Input:**
```text
FreqStack fs = new FreqStack();
fs.push(1);
fs.push(2);
fs.pop();
```

**Output:**
```text
[null, null, null, 2]
```

**Explanation:**
Tied frequency 1 pops most recent element 2.

### Example 3

**Input:**
```text
FreqStack fs = new FreqStack();
fs.push(9);
fs.pop();
```

**Output:**
```text
[null, null, 9]
```

**Explanation:**
Pops 9.

---

## Constraints

- `0 <= val <= 10^9`
- At most `2 * 10^4` calls will be made to `push` and `pop`.
- It is guaranteed that there will be at least one element in the stack before calling `pop`.

---

## Complexity Analysis

- **Time Complexity**: `O(1) for both push and pop`
- **Space Complexity**: `O(N)`
