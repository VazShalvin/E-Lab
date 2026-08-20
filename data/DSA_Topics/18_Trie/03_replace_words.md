# 3. Replace Words (Root Replacement with Trie)

**Topic**: Trie  
**Difficulty**: Medium  
**Tags**: Array, Hash Table, String, Trie

---

## Problem Statement

In English, we have a concept called **root**, which can be followed by some other word to form another longer word - let's call this word **derivative**. For example, when the root `"help"` is followed by the derivative `"ful"`, we can form a new word `"helpful"`.

Given a `dictionary` consisting of many roots and a `sentence` consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the **shortest length**.

Return the sentence after the replacement.

---

## Input & Output Format

- **Input**: A list of strings `dictionary` and a string `sentence`.
- **Output**: A replaced sentence string.

---

## Sample Test Cases

### Example 1

**Input:**
```text
dictionary = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"
```

**Output:**
```text
"the cat was rat by the bat"
```

**Explanation:**
cattle -> cat, rattled -> rat, battery -> bat.

### Example 2

**Input:**
```text
dictionary = ["a", "b", "c"], sentence = "aadsfasf absbs bbab cadsfafs"
```

**Output:**
```text
"a a b c"
```

**Explanation:**
All words shortened to single character roots.

### Example 3

**Input:**
```text
dictionary = ["catt", "cat"], sentence = "cattle"
```

**Output:**
```text
"cat"
```

**Explanation:**
Shortest matching root "cat" is chosen.

---

## Constraints

- `1 <= dictionary.length <= 1000`
- `1 <= dictionary[i].length <= 100`
- `1 <= sentence.length <= 10^6`
- `dictionary[i]` and `sentence` consist of only lowercase letters and spaces.

---

## Complexity Analysis

- **Time Complexity**: `O(N * L + M)`
- **Space Complexity**: `O(N * L)`
