# 6. Serialize and Deserialize Binary Tree

**Topic**: Binary Tree  
**Difficulty**: Hard  
**Tags**: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree

---

## Problem Statement

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

---

## Input & Output Format

- **Input**: Binary tree root for serialization / serialized string for deserialization.
- **Output**: Serialized string / Deserialized binary tree identical to input.

---

## Sample Test Cases

### Example 1

**Input:**
```text
root = [1, 2, 3, null, null, 4, 5]
```

**Output:**
```text
[1, 2, 3, null, null, 4, 5]
```

**Explanation:**
Serialized to a compact string (e.g. "1,2,null,null,3,4,null,null,5,null,null") and deserialized back accurately.

### Example 2

**Input:**
```text
root = []
```

**Output:**
```text
[]
```

**Explanation:**
Empty tree serializes to "null" and deserializes back to null.

### Example 3

**Input:**
```text
root = [1]
```

**Output:**
```text
[1]
```

**Explanation:**
Single node tree is preserved.

---

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-1000 <= Node.val <= 1000`

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
