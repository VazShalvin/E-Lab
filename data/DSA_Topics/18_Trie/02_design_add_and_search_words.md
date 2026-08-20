# 2. Design Add and Search Words Data Structure

**Topic**: Trie  
**Difficulty**: Medium  
**Tags**: String, Depth-First Search, Design, Trie

---

## Problem Statement

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:
- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

---

## Input & Output Format

- **Input**: Method calls and parameters.
- **Output**: Output values corresponding to search calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

**Output:**
```text
[null, null, null, null, false, true, true, true]
```

**Explanation:**
'.' matches any character recursively through the Trie.

### Example 2

**Input:**
```text
wd.search("....");
```

**Output:**
```text
false
```

**Explanation:**
No 4-letter word inserted.

### Example 3

**Input:**
```text
wd.addWord("a"); wd.search(".");
```

**Output:**
```text
[null, true]
```

**Explanation:**
'.' matches 'a'.

---

## Constraints

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consist of `'.'` or lowercase English letters.
- At most `10^4` calls will be made to `addWord` and `search`.

---

## Complexity Analysis

- **Time Complexity**: `O(L) addWord, O(26^D * L) search with D dots`
- **Space Complexity**: `O(Total Characters)`
