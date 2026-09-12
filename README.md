# LeetCode 186 - Reverse Words in a String II

## Problem

Given a character array representing a sentence, reverse the order of the words in the sentence.

The input is provided as an array of characters, so the string must be modified **in-place**.

For example:

```text
Input:
the sky is blue

Output:
blue is sky the
```

## Approach

The solution can be done in two main steps.

### Step 1: Reverse the Entire String

First, reverse all characters in the sentence.

For example:

```text
the sky is blue
```

becomes:

```text
eulb si yks eht
```

### Step 2: Reverse Each Individual Word

After reversing the complete string, each individual word is also reversed.

So we reverse every word separately:

```text
eulb → blue
si   → is
yks  → sky
eht  → the
```

The final result becomes:

```text
blue is sky the
```

## Python Program

```python
class Solution:
    def reverseWords(self, s):
        s = list(s)

        s.reverse()

        start = 0

        for i in range(len(s) + 1):
            if i == len(s) or s[i] == ' ':
                s[start:i] = reversed(s[start:i])
                start = i + 1

        return ''.join(s)
```

## Example

### Input

```text
["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
```

### Output

```text
["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
```

## Key Idea

The important trick is:

**Reverse the entire string → reverse each word.**

This changes the order of the words while keeping the characters inside each word in their correct order.

## Why Use a Character Array?

The problem requires the sentence to be modified **in-place**.

Therefore, the characters are handled as a list rather than directly creating a completely new sentence.

## Time Complexity

**O(n)**

Each character is processed a constant number of times.

Where `n` is the length of the character array.

## Space Complexity

**O(n)**

The Python implementation converts the input into a list of characters.

The algorithm itself uses only a small amount of extra working space apart from the character array.

## Difficulty

**Medium**

## Topics

* Strings
* Arrays
* Two-pointer technique
* In-place manipulation
* String reversal

## What I Learned

This problem helped me understand how reversing operations can be combined to change the order of words without individually moving every word.

The main logic is:

```text
Reverse everything
        ↓
Reverse every word
        ↓
Words appear in reverse order
```

## Author

T.Nandhini
