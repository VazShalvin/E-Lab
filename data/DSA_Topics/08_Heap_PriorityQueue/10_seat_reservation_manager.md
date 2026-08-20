# 10. Seat Reservation Manager

**Topic**: Heap / Priority Queue  
**Difficulty**: Medium  
**Tags**: Design, Heap

---

## Problem Statement

Design a system that manages the reservation state of `n` seats that are numbered from `1` to `n`.

Implement the `SeatManager` class:
- `SeatManager(int n)` Initializes a `SeatManager` object that will manage `n` seats numbered from `1` to `n`. All seats are initially available.
- `int reserve()` Fetches the **smallest-numbered** unreserved seat, reserves it, and returns its number.
- `void unreserve(int seatNumber)` Unreserves the seat with the given `seatNumber`.

---

## Input & Output Format

- **Input**: Method calls and parameters.
- **Output**: Output list corresponding to reserve calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
SeatManager seatManager = new SeatManager(5);
seatManager.reserve();    // returns 1
seatManager.reserve();    // returns 2
seatManager.unreserve(2); // unreserve seat 2
seatManager.reserve();    // returns 2 (smallest available)
seatManager.reserve();    // returns 3
seatManager.reserve();    // returns 4
seatManager.reserve();    // returns 5
seatManager.unreserve(5); // unreserve seat 5
```

**Output:**
```text
[null, 1, 2, null, 2, 3, 4, 5, null]
```

**Explanation:**
Min-heap always delivers the lowest numbered free seat.

### Example 2

**Input:**
```text
SeatManager sm = new SeatManager(2); sm.reserve();
```

**Output:**
```text
[null, 1]
```

**Explanation:**
Seat 1 is reserved.

### Example 3

**Input:**
```text
sm.reserve(); sm.unreserve(1); sm.reserve();
```

**Output:**
```text
[2, null, 1]
```

**Explanation:**
Seat 1 recycled.

---

## Constraints

- `1 <= n <= 10^5`
- `1 <= seatNumber <= n`
- For each call to `reserve`, it is guaranteed there is at least one unreserved seat.
- For each call to `unreserve`, it is guaranteed `seatNumber` will be reserved.

---

## Complexity Analysis

- **Time Complexity**: `O(log N) for reserve and unreserve`
- **Space Complexity**: `O(N)`
