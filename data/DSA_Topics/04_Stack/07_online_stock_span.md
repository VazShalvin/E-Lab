# 7. Online Stock Span

**Topic**: Stack  
**Difficulty**: Medium  
**Tags**: Stack, Design, Monotonic Stack, Data Stream

---

## Problem Statement

Design an algorithm that collects daily price quotes for some stock and returns the **span** of that stock's price for the current day.

The **span** of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

Implement the `StockSpanner` class:
- `StockSpanner()` Initializes the object of the class.
- `int next(int price)` Returns the span of the stock's price given that today's price is `price`.

---

## Input & Output Format

- **Input**: Method calls with price values.
- **Output**: Integer span value for each call.

---

## Sample Test Cases

### Example 1

**Input:**
```text
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4
stockSpanner.next(85);  // return 6
```

**Output:**
```text
[null, 1, 1, 1, 2, 1, 4, 6]
```

**Explanation:**
On day 6, price 85 is greater than or equal to previous prices (75, 60, 70, 60, 80), so span is 6.

### Example 2

**Input:**
```text
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(10);
stockSpanner.next(20);
stockSpanner.next(30);
```

**Output:**
```text
[null, 1, 2, 3]
```

**Explanation:**
Strictly increasing prices give spans 1, 2, 3.

### Example 3

**Input:**
```text
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(50);
stockSpanner.next(40);
stockSpanner.next(30);
```

**Output:**
```text
[null, 1, 1, 1]
```

**Explanation:**
Strictly decreasing prices give span 1 each day.

---

## Constraints

- `1 <= price <= 10^5`
- At most `10^4` calls will be made to `next`.

---

## Complexity Analysis

- **Time Complexity**: `O(1) amortized per call`
- **Space Complexity**: `O(N)`
