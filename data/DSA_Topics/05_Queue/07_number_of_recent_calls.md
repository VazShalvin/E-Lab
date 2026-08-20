# 7. Number of Recent Calls

**Topic**: Queue  
**Difficulty**: Easy  
**Tags**: Design, Queue, Data Stream

---

## Problem Statement

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:
- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that has happened in the past `3000` milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is guaranteed that every call to `ping` uses a strictly larger value of `t` than the previous call.

---

## Input & Output Format

- **Input**: Sequential `ping(t)` calls.
- **Output**: Integer count of pings in window `[t-3000, t]`.

---

## Sample Test Cases

### Example 1

**Input:**
```text
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // returns 1
recentCounter.ping(100);   // returns 2
recentCounter.ping(3001);  // returns 3
recentCounter.ping(3002);  // returns 3 (ping at time 1 is outside [2, 3002])
```

**Output:**
```text
[null, 1, 2, 3, 3]
```

**Explanation:**
Pings older than t - 3000 are evicted from the queue.

### Example 2

**Input:**
```text
RecentCounter rc = new RecentCounter();
rc.ping(6000);
```

**Output:**
```text
[null, 1]
```

**Explanation:**
Single ping at time 6000.

### Example 3

**Input:**
```text
RecentCounter rc = new RecentCounter();
rc.ping(10);
rc.ping(10000);
```

**Output:**
```text
[null, 1, 1]
```

**Explanation:**
Time 10 is evicted by time 10000.

---

## Constraints

- `1 <= t <= 10^9`
- Each test case will call `ping` with strictly increasing values of `t`.
- At most `10^4` calls will be made to `ping`.

---

## Complexity Analysis

- **Time Complexity**: `O(1) amortized per ping`
- **Space Complexity**: `O(W) where W <= 3000`
