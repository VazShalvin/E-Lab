# 12. Simplify Path

**Topic**: Stack  
**Difficulty**: Medium  
**Tags**: String, Stack

---

## Problem Statement

Given an absolute path for a Unix-style file system, simplify it. In a Unix-style file system, a period `'.'` refers to the current directory, a double period `'..'` refers to the directory up a level, and any multiple consecutive slashes (i.e. `'//'`) are treated as a single slash `'/'`.

The canonical path should follow these rules:
- The path starts with a single slash `'/'`.
- Any two directories are separated by a single slash `'/'`.
- The path does not end with a trailing `'/'`.
- The path only contains the directories on the path from the root directory to the target file or directory.

---

## Input & Output Format

- **Input**: An absolute string path `path`.
- **Output**: Simplified canonical path string.

---

## Sample Test Cases

### Example 1

**Input:**
```text
path = "/home/"
```

**Output:**
```text
"/home"
```

**Explanation:**
Trailing slash removed.

### Example 2

**Input:**
```text
path = "/../"
```

**Output:**
```text
"/"
```

**Explanation:**
Going up from root remains root.

### Example 3

**Input:**
```text
path = "/home//foo/"
```

**Output:**
```text
"/home/foo"
```

**Explanation:**
Multiple consecutive slashes are replaced by a single slash.

---

## Constraints

- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `'.'`, slash `'/'` or `'_'`.
- `path` is a valid absolute Unix path.

---

## Complexity Analysis

- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
