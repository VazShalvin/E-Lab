# 9. Assign Cookies

**Topic**: Greedy  
**Difficulty**: Easy  
**Tags**: Array, Two Pointers, Greedy, Sorting

---

## Problem Statement

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

---

## Input & Output Format

- **Input**: Two arrays `g` and `s`.
- **Output**: An integer representing count of content children.

---

## Sample Test Cases

### Example 1

**Input:**
```text
g = [1, 2, 3], s = [1, 1]
```

**Output:**
```text
1
```

**Explanation:**
You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.

### Example 2

**Input:**
```text
g = [1, 2], s = [1, 2, 3]
```

**Output:**
```text
2
```

**Explanation:**
Both children can be satisfied.

### Example 3

**Input:**
```text
g = [3, 4], s = [1, 2, 2]
```

**Output:**
```text
0
```

**Explanation:**
No child can be satisfied.

---

## Constraints

- `1 <= g.length <= 3 * 10^4`
- `0 <= s.length <= 3 * 10^4`
- `1 <= g[i], s[j] <= 2^31 - 1`

---

## Complexity Analysis

- **Time Complexity**: `O(N log N + M log M)`
- **Space Complexity**: `O(1)`
