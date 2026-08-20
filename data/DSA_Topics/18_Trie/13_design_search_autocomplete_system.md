# 13. Design Search Autocomplete System

**Topic**: Trie  
**Difficulty**: Hard  
**Tags**: String, Design, Trie, Heap, Data Stream

---

## Problem Statement

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character `'#'`).

You are given a string array `sentences` and an integer array `times` both of length `n`.

Implement the `AutocompleteSystem` class:
- `AutocompleteSystem(String[] sentences, int[] times)` Initializes the object with historical data.
- `List<String> input(char c)` Returns the **top 3 historical hot sentences** that have the same prefix as the current input characters typed so far. If fewer than 3 hot sentences exist, return as many as possible.

---

## Input & Output Format

- **Input**: Method calls and typed characters.
- **Output**: List of top 3 hot sentences.

---

## Sample Test Cases

### Example 1

**Input:**
```text
AutocompleteSystem sys = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
sys.input('i'); // return ["i love you", "island", "i love leetcode"]
sys.input(' '); // return ["i love you", "i love leetcode"]
sys.input('a'); // return []
sys.input('#'); // ends sentence, return []
```

**Output:**
```text
[["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]
```

**Explanation:**
Trie nodes store references/frequencies of sentences for top-3 recommendations.

### Example 2

**Input:**
```text
sys.input('i');
```

**Output:**
```text
["i love you", "i love leetcode", "i love a"]
```

**Explanation:**
Updated frequency included.

### Example 3

**Input:**
```text
sys.input('#');
```

**Output:**
```text
[]
```

**Explanation:**
Terminates sentence.

---

## Constraints

- `n == sentences.length == times.length`
- `1 <= n <= 100`
- `1 <= sentences[i].length <= 100`
- `1 <= times[i] <= 50`
- `c` is a lowercase English letter, `' '`, or `'#'`.
- At most `5000` calls will be made to `input`.

---

## Complexity Analysis

- **Time Complexity**: `O(P) per typed character where P is prefix match size`
- **Space Complexity**: `O(Total Historical Characters)`
