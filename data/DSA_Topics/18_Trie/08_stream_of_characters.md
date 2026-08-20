# 8. Stream of Characters (Reverse Trie)

**Topic**: Trie  
**Difficulty**: Hard  
**Tags**: Array, String, Design, Trie, Data Stream

---

## Problem Statement

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings `words`.

Implement the `StreamChecker` class:
- `StreamChecker(String[] words)` Initializes the object with the dictionary of words.
- `boolean query(char letter)` Accepts a new character from the stream and returns `true` if some non-empty suffix from the stream equals a word in `words`, or `false` otherwise.

---

## Input & Output Format

- **Input**: Constructor word list and stream of single characters.
- **Output**: List of booleans corresponding to query calls.

---

## Sample Test Cases

### Example 1

**Input:**
```text
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query('a'); // return False
streamChecker.query('b'); // return False
streamChecker.query('c'); // return False
streamChecker.query('d'); // return True, because 'cd' is in the wordlist
streamChecker.query('e'); // return False
streamChecker.query('f'); // return True, because 'f' is in the wordlist
```

**Output:**
```text
[null, false, false, false, true, false, true]
```

**Explanation:**
Words are stored in reverse in the Trie so stream query matches backwards in O(max_word_len).

### Example 2

**Input:**
```text
StreamChecker sc = new StreamChecker(["ab", "ba"]); sc.query('a'); sc.query('b');
```

**Output:**
```text
[false, true]
```

**Explanation:**
"ab" matched.

### Example 3

**Input:**
```text
sc.query('a');
```

**Output:**
```text
true
```

**Explanation:**
Suffix "ba" matched.

---

## Constraints

- `1 <= words.length <= 2000`
- `1 <= words[i].length <= 200`
- `words[i]` consists of lowercase English letters.
- `letter` is a lowercase English letter.
- At most `4 * 10^4` calls will be made to `query`.

---

## Complexity Analysis

- **Time Complexity**: `O(max_len) per query`
- **Space Complexity**: `O(Total Characters in words + stream history)`
