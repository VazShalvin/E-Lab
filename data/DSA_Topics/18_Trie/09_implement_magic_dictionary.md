# 9. Implement Magic Dictionary

**Topic**: Trie  
**Difficulty**: Medium  
**Tags**: Hash Table, String, Depth-First Search, Design, Trie

---

## Problem Statement

Design a data structure that is initialized with a list of **different** words. Provided a new string, you should determine if you can change **exactly one character** in this string to match any word in the data structure.

Implement the `MagicDictionary` class:
- `MagicDictionary()` Initializes the object.
- `void buildDict(String[] dictionary)` Sets the data structure with an array of distinct strings `dictionary`.
- `bool search(String searchWord)` Returns `true` if you can change exactly one character in `searchWord` to match any string in the data structure, otherwise returns `false`.

---

## Input & Output Format

- **Input**: Method calls and parameters.
- **Output**: Booleans for search calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False (must change exactly 1 char)
magicDictionary.search("hhllo"); // return True (change 'h' to 'e')
magicDictionary.search("hell");  // return False (different length)
magicDictionary.search("leetcoded"); // return False
```

**Output:**
```text
[null, null, false, true, false, false]
```

**Explanation:**
Trie search tracks exactly 1 modification allowed.

### Example 2

**Input:**
```text
md.buildDict(["hello", "hallo"]); md.search("hello");
```

**Output:**
```text
[null, true]
```

**Explanation:**
Change 'e' to 'a' matches "hallo".

### Example 3

**Input:**
```text
md.search("world");
```

**Output:**
```text
false
```

**Explanation:**
No 1-char change match.

---

## Constraints

- `1 <= dictionary.length <= 100`
- `1 <= dictionary[i].length <= 100`
- `dictionary[i]` consists of only lower-case English letters.
- All strings in `dictionary` are **distinct**.
- `1 <= searchWord.length <= 100`
- At most `100` calls will be made to `search`.

---

## Complexity Analysis

- **Time Complexity**: `O(L) buildDict, O(26 * L) search`
- **Space Complexity**: `O(Total Characters)`
